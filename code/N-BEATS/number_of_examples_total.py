import pickle as pkl

for d in ['carbs', 'bolus', 'combo']:
	fd = open('num_examples_' + d + '.txt', 'w')
	for c in ['1', '3']:
		fd.write('CASE: ' + c + '\n')
		for s in ['training', 'validation', 'testing']:
			fd.write(s + '\n')
			fd2 = open(d + '_data.pkl', 'rb')
			data = pkl.load(fd2)
			fd2.close()
			total = 0
			for p in ['540', '544', '552', '559', '563', '567', '570', '575', '584', '588', '591', '596']:
			#for p in ['540', '544', '552', '567', '584', '596']:
			#for p in ['559', '563', '570', '575', '588', '591']:
				total += len(data[0][s][1][p][c])
			fd.write(str(total) + '\n')
		
fd.close()
