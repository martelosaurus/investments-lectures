import numpy as np
import pandas as pd
import re

# stck: date ticker coname markret riskfree dividend price ret div_gro_rat req_ret
# bond: cusip iss_date cal_date mat_date price sa_yield coupon_rate

# parameters
n = 6

# open all of the relevant files
data_path = '/home/jordan/Dropbox/Investments2020Martel/data/'
air = pd.read_csv(data_path+'stcks/portairlinesdemo.csv',dtype='str')

# create problems
prob_file = open('asset_classes_problems','r')
problems = prob_file.read()
problems = problems[:-1].split('\n\n')
for problem in problems:
	for j in range(0,n):
		temp, problem_code, data_set, Q, A = re.split(':: ',problem)
		this_port = air.sample(1).to_dict('records')[0]
		Q = Q.format(**this_port)
		A = A.format(**this_port)

		# question
		qstn_file = open('problems/' + problem_code[:-1] + str(j) + 'Q.tex','w')
		qstn_file.write(Q)
		qstn_file.close()

		# answer
		ansr_file = open('problems/' + problem_code[:-1] + str(j) + 'A.tex','w')
		ansr_file.write(A)
		ansr_file.close()
	
# close everythin 
prob_file.close()
