import torch
from torch.utils.data import TensorDataset
import numpy as np
import pickle

def load_data(filename, pretrain=False, patient=None, unrestricted=True, combined=False):
	fd = open(filename, 'rb')
	if pretrain:
		(_, data) = pickle.load(fd)
	else:
		(data, _) = pickle.load(fd)
		
	fd.close()
	
	if pretrain:
		scaling = data['scaling']
	else:
		scaling = data['scaling'][patient]
	
	(training_x, training_y) = data['training']
	(validation_x, validation_y) = data['validation']
	(testing_x, testing_y) = data['testing']
	
	if unrestricted:
		case = '3'
	else:
		case = '1'
	
	if pretrain:
		tr_x = training_x[case]['input1_layer']
		tr_x2 = training_x[case]['input3_layer']
		tr_x3 = training_x[case]['input2_layer']
		tr_y = training_y[case]
		
		va_x = validation_x[case]['input1_layer']
		va_x2 = validation_x[case]['input3_layer']
		va_x3 = validation_x[case]['input2_layer']
		va_y = validation_y[case]
		
		te_x = testing_x[case]['input1_layer']
		te_x2 = testing_x[case]['input3_layer']
		te_x3 = testing_x[case]['input2_layer']
		te_y = testing_y[case]
		
	else:
		tr_x = training_x[patient][case]['input1_layer']
		tr_x2 = training_x[patient][case]['input3_layer']
		tr_x3 = training_x[patient][case]['input2_layer']
		tr_y = training_y[patient][case]
		
		va_x = validation_x[patient][case]['input1_layer']
		va_x2 = validation_x[patient][case]['input3_layer']
		va_x3 = validation_x[patient][case]['input2_layer']
		va_y = validation_y[patient][case]
		
		te_x = testing_x[patient][case]['input1_layer']
		te_x2 = testing_x[patient][case]['input3_layer']
		te_x3 = testing_x[patient][case]['input2_layer']
		te_y = testing_y[patient][case]
	
	if combined:
		print('COMBINED')
		tr_x = np.append(tr_x, va_x, axis=0)
		tr_x2 = np.append(tr_x2, va_x2, axis=0)
		tr_x3 = np.append(tr_x3, va_x3, axis=0)
		tr_y = np.append(tr_y, va_y, axis=0)
		
	training_dataset = TensorDataset(torch.from_numpy(tr_x).type(torch.float), 
									 torch.from_numpy(tr_x2).type(torch.float), 
									 torch.from_numpy(tr_x3).type(torch.float), 
									 torch.from_numpy(tr_y).unsqueeze(1).type(torch.float))
									 
	testing_dataset = TensorDataset(torch.from_numpy(te_x).type(torch.float), 
									torch.from_numpy(te_x2).type(torch.float), 
									torch.from_numpy(te_x3).type(torch.float), 
									torch.from_numpy(te_y).unsqueeze(1).type(torch.float))
									
	validation_dataset = TensorDataset(torch.from_numpy(va_x).type(torch.float), 
									   torch.from_numpy(va_x2).type(torch.float), 
									   torch.from_numpy(va_x3).type(torch.float), 
									   torch.from_numpy(va_y).unsqueeze(1).type(torch.float))
	
	return ((training_dataset, testing_dataset, validation_dataset), scaling)
