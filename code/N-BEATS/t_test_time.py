from scipy import stats
import numpy as np
import json

taus = ['30', '45', '60', '75', '90']

best = {
	'carbs': 'AVG',
	'bolus': 'AVG',
	'combo': 'AVG'
}

patient_lists = {
	'carbs': ['540', '544', '552', '559', '563', '575', '584', '588', '591', '596'],
	'bolus': ['540', '552', '559', '563', '570', '575', '584', '588', '591', '596'],
	'combo': ['540', '544', '552', '559', '563', '575', '584', '588', '591']
}

one_v_all = {
	'carbs': {
		'RMSE': {'30': True, '45': False, '60': False, '75': False, '90': False}, 
		'MAE': {'30': False, '45': False, '60': False, '75': False, '90': False}
	},
	'bolus': {
		'RMSE': {'30': False, '45': True, '60': False, '75': True, '90': False}, 
		'MAE': {'30': False, '45': True, '60': False, '75': False, '90': False}
	},
	'combo': {
		'RMSE': {'30': False, '45': False, '60': False, '75': False, '90': False}, 
		'MAE': {'30': False, '45': False, '60': False, '75': False, '90': False}
	}
}

p_values = {}

for s in ['carbs', 'bolus', 'combo']:
	p_values[s] = {'RMSE': {}, 'MAE': {}}
	for t in taus:
		p_values[s]['RMSE'][t] = {}
		p_values[s]['MAE'][t] = {}
		
		fd1 = open('./time/' + s + '/' + t + '/all.json', 'r')
		fd2 = open('./time/' + s + '/' + t + '/one.json', 'r')
		
		all_tau = json.load(fd1)
		one_tau = json.load(fd2)
		
		fd1.close()
		fd2.close()
		
		all_rmse = []
		all_mae = []
		
		one_rmse = []
		one_mae = []
		
		for p in patient_lists[s]:
			all_rmse.append(all_tau['by_patient'][best[s]][p]['RMSE'])
			all_mae.append(all_tau['by_patient'][best[s]][p]['MAE'])
			
			one_rmse.append(one_tau['by_patient'][best[s]][p]['RMSE'])
			one_mae.append(one_tau['by_patient'][best[s]][p]['MAE'])
			
		all_rmse = np.array(all_rmse)
		all_mae = np.array(all_mae)
		
		one_rmse = np.array(one_rmse)
		one_mae = np.array(one_mae)

		if one_v_all[s]['RMSE'][t]:
			p_rmse = stats.ttest_rel(one_rmse, all_rmse, alternative='less').pvalue
			p_values[s]['RMSE'][t]['one_v_all'] = p_rmse
		else:
			p_rmse = stats.ttest_rel(all_rmse, one_rmse, alternative='less').pvalue
			p_values[s]['RMSE'][t]['all_v_one'] = p_rmse
			
		if one_v_all[s]['MAE'][t]:
			p_mae = stats.ttest_rel(one_mae, all_mae, alternative='less').pvalue
			p_values[s]['MAE'][t]['one_v_all'] = p_mae
		else:
			p_mae = stats.ttest_rel(all_mae, one_mae, alternative='less').pvalue
			p_values[s]['MAE'][t]['all_v_one'] = p_mae
		
fd = open('p_values_time.json', 'w')
json.dump(p_values, fd, indent=4)
