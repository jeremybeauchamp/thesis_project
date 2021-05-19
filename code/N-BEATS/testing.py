#!/home/jb199113/anaconda3/bin/python

# This file is used to evaluate the trained models

import torch
from torch.utils.data import DataLoader
import numpy as np
from load_data import load_data
import json
import argparse
	
def RMSE(predictions, labels):
	rmse = (predictions - labels) ** 2
	rmse = np.mean(rmse)
	rmse = np.sqrt(rmse)
	return rmse
	
	
def MAE(predictions, labels):
	mae = np.abs(predictions - labels)
	mae = np.mean(mae)
	return mae
	
# This is the primary function used to evaluate the trained models
#
# Parameters:
#	data = the data returned from the load_data function
#
#	patient_list = the list of patient IDs
#
#	scaling = the parameters used to scale the data
#
#	batch_size = the size of batches of examples
#
#	testing_set = 'training', 'testing', or 'validation'
#
#	unrestricted = True if unrestricted, False for inertial
#
#	runs = number of runs per subject
#
#	tensorboard = True if tensorboard logs should be generated

def evaluate(data, 
			 patient_list,
			 scaling,
			 batch_size,
			 testing_set='validation', 
			 unrestricted=True, 
			 runs=1, 
			 tensorboard=False):
			 
	torch.manual_seed(0)
	np.random.seed(0)
	
	if torch.cuda.is_available():
		device = torch.device('cuda')
	else:
		device = torch.device('cpu')
	
	results = {}
	best_models = {}
	for patient in patient_list:
		(training, testing, validation) = data[patient]
					
		if testing_set == 'training':
			dataset = training
		elif testing_set == 'validation':
			dataset = validation
		elif testing_set == 'testing':
			dataset = testing
			
		testing_loader = DataLoader(dataset=dataset,
									shuffle=True,
									drop_last=False)
									
		validation_loader = DataLoader(dataset=validation,
									   shuffle=True,
									   drop_last=False)
									
		scale_min = scaling[patient]['min']
		scale_max = scaling[patient]['max']
		
		best_mae = np.inf
		best_models[patient] = 0
		for run in range(runs): 
			network = torch.load('./patient_' + patient + '_' + str(run) + '.model').get('model').cuda()
			
			network.eval()
			
			predictions = []
			labels = [] 
			for step, (vx, vx2, vx3, vy) in enumerate(validation_loader):
				with torch.no_grad():
				
					if unrestricted:
						prediction, _, _, _, _ = network(vx.to(device), vx2.to(device), x3=vx3.to(device))
					else:
						prediction, _, _, _, _ = network(vx.to(device), vx2.to(device))

				predictions = predictions + prediction.cpu().data.numpy().tolist()
				labels = labels + vy.cpu().data.numpy().tolist()
				
			predictions = np.asarray(predictions)
			labels = np.asarray(labels)
			
			predictions = (predictions * scale_max) + scale_min
			labels = (labels * scale_max) + scale_min
			mae = MAE(predictions, labels)
			
			if mae < best_mae:
				best_mae = mae
				best_models[patient] = run

		results[patient] = {'RMSEs': [], 'MAEs': []}
		for run in range(runs):
			fd = open('errors_' + str(patient) + '_' + str(run) + '.txt', 'w')
			np.random.seed(run)
			torch.manual_seed(run)
		
			network = torch.load('./patient_' + patient + '_' + str(run) + '.model').get('model').cuda()
			
			network.eval()
			
			predictions = []
			labels = [] 
			 
			for step, (x, x2, x3, y) in enumerate(testing_loader):
				with torch.no_grad():
				
					if unrestricted:
						prediction, _, _, _, _ = network(x.to(device), x2.to(device), x3=x3.to(device))
					else:
						prediction, _, _, _, _ = network(x.to(device), x2.to(device))
	
				fd.write(str((prediction.cpu().data.numpy()[0][0] * scale_max) + scale_min) + ',' + str((y.cpu().data.numpy()[0][0] * scale_max) + scale_min) + '\n')
				predictions = predictions + prediction.cpu().data.numpy().tolist()
				labels = labels + y.cpu().data.numpy().tolist()
				
			fd.close()
			predictions = np.asarray(predictions)
			labels = np.asarray(labels)
			
			predictions = (predictions * scale_max) + scale_min
			labels = (labels * scale_max) + scale_min
			rmse = RMSE(predictions, labels)
			mae = MAE(predictions, labels)
			results[patient]['RMSEs'].append(rmse)
			results[patient]['MAEs'].append(mae)
			
	return (results, best_models)
	

def compute_final_results(results, best_models, patient_list):
	bests = {}
	averages = {}
	for p in patient_list:
		best_rmse = 0
		best_mae = 0
		average_rmse = 0
		average_mae = 0
		for r in range(len(results[p]['MAEs'])):
			average_rmse = average_rmse + results[p]['RMSEs'][r]
			average_mae = average_mae + results[p]['MAEs'][r]
			
			if r == best_models[p]:
				best_rmse = results[p]['RMSEs'][r]
				best_mae = results[p]['MAEs'][r]
				
		average_rmse = average_rmse / len(results[p]['MAEs'])
		average_mae = average_mae / len(results[p]['MAEs'])
		
		bests[p] = {'RMSE': best_rmse, 'MAE': best_mae}
		averages[p] = {'RMSE': average_rmse, 'MAE': average_mae}
		
	average_rmse = 0
	average_mae = 0
	best_rmse = 0
	best_mae = 0
	for p in patient_list:
		average_rmse = average_rmse + averages[p]['RMSE']
		average_mae = average_mae + averages[p]['MAE']
		best_rmse = best_rmse + bests[p]['RMSE']
		best_mae = best_mae + bests[p]['MAE']
		
	average_rmse = average_rmse / len(patient_list)
	average_mae = average_mae / len(patient_list)
	best_rmse = best_rmse / len(patient_list)
	best_mae = best_mae / len(patient_list)
	
	overall = {'AVG': {'RMSE': average_rmse, 'MAE': average_mae}, 
			   'BEST': {'RMSE': best_rmse, 'MAE': best_mae}
			  }
			  
	by_patient = {'AVG': averages, 'BEST': bests}
			
	return {'by_patient': by_patient, 'overall': overall}

				
	
if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('--scenario', default='carbs', type=str)
	parser.add_argument('--case', default='unrestricted', type=str)
	parser.add_argument('--time', default=0, type=int)
	parser.add_argument('--combined', default='False', type=str)
	parser.add_argument('--runs', default=5, type=int)
	args = parser.parse_args()
	
	scenario = args.scenario
	
	time = args.time
		
	if args.combined == 'True':
		combined = True
	else:
		combined = False
		
	case = args.case
	if case == 'unrestricted':
		unrestricted = True
	else:
		unrestricted = False
		
	runs = args.runs
	
	if scenario == 'carbs':
		patient_list = ['540', '544', '552', '559', '563', '575', '584', '588', '591', '596']
	elif scenario == 'combo':
		patient_list = ['540', '544', '552', '559', '563', '575', '584', '588', '591']
	else:
		patient_list = ['540', '552', '559', '563', '570', '575', '584', '588', '591', '596']
		
	if time == 0:
		filename = scenario + '_data.pkl'
	else:
		filename = scenario + '_data' + str(time) + '.pkl'
		
	data = {}
	scaling = {}
	for p in patient_list:
		(data_p, scaling_p) = load_data(filename, pretrain=False, patient=p, unrestricted=unrestricted, combined=combined)
		
		data[p] = data_p
		scaling[p] = scaling_p
		
	fd = open(scenario + '_hyper_parameters_' + case + '.json', 'r')
	hyper_parameters = json.load(fd)
	fd.close()
	
	batch_size = hyper_parameters['batch_size']
	
	results, best_models = evaluate(data, 
									patient_list, 
									scaling, 
									batch_size,
									testing_set='testing',
									unrestricted=unrestricted, 
									runs=runs, 
									tensorboard=True)
	
	final_results = compute_final_results(results, best_models, patient_list)
			
	fd = open('results.json', 'w')	
	json.dump(final_results, fd)
	fd.close()
			
			
			
			
