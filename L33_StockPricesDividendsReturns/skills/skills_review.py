import numpy as np
import pandas as pd
import re

# stck: date ticker coname markret riskfree dividend price ret div_gro_rat req_ret
# bond: cusip iss_date cal_date mat_date price sa_yield coupon_rate

# parameters
n = 6

# open all of the relevant files
data_path = '/home/jordan/Dropbox/Investments2020Martel/data/'
stck = pd.read_csv(data_path+'stcks/stck_dataset_jordan.csv',dtype='str')
bond = pd.read_csv(data_path+'bonds/DPMT_bond_dataset_jordan.csv',dtype='str')

# full observations
#stck = stck.dropna()
bond = bond.dropna()

# create problems
prob_file = open('skills_review_problems','r')
problems = prob_file.read()
problems = problems[:-1].split('\n\n')
for problem in problems:
	for j in range(0,n):
		temp, problem_code, data_set, Q, A = re.split(':: ',problem)
		if data_set[:-1] == 'stcks':		
			this_stck = stck.sample(1).to_dict('records')[0]
			Q = Q.format(**this_stck)
			A = A.format(**this_stck)
		elif data_set[:-1] == 'bonds':
			this_bond = bond.sample(1).to_dict('records')[0]
			Q = Q.format(**this_bond)
			A = A.format(**this_bond)
		else:
			print('unspecified asset')

		# question
		qstn_file = open('problems/' + problem_code[:-1] + str(j) + 'Q.tex','w')
		qstn_file.write(Q)
		qstn_file.close()

		# answer
		ansr_file = open('problems/' + problem_code[:-1] + str(j) + 'A.tex','w')
		ansr_file.write('\\begin{align*}\n')
		ansr_file.write(A + '\n')
		ansr_file.write('\\end{align*}\n')
		ansr_file.close()
	
# close everythin 
prob_file.close()
