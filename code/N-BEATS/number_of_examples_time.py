import pickle as pkl

for d in ['carbs', 'bolus', 'combo']:
	fd = open('num_examples_' + d + '.txt', 'w')
	for c in ['1']:
		fd.write('CASE: ' + c + '\n')
		for s in ['training', 'validation', 'testing']:
			fd.write(s + '\n')
			fd2 = open(d + '_data.pkl', 'rb')
			data = pkl.load(fd2)
			fd2.close()
			times = {'30': 0, '45': 0, '60': 0, '75': 0, '90': 0}
			for p in ['540', '544', '552', '559', '563', '567', '570', '575', '584', '588', '591', '596']:
				for i in range(len(data[0][s][1][p][c])):
					time = data[0][s][0][p][c]['input3_layer'][i][1] * 95
					
					if time == 30:
						times['30'] += 1
					elif time == 45:
						times['45'] += 1
					elif time == 60:
						times['60'] += 1
					elif time == 75:
						times['75'] += 1
					elif time == 90:
						times['90'] += 1
		
			for i in times.keys():
				fd.write(i + ' = ' + str(times[i]) + '\n')
		
fd.close()
