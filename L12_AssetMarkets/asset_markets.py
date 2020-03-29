import numpy as np
import pandas as pd
import re

# parameters
n = 6
imr_req = .5
imr_act = .75

# open all of the relevant files
data_path = '/home/jordan/Dropbox/Investments2020Martel/data/'
stck =  pd.read_csv(data_path+'stcks/stck_dataset_jordan.csv',dtype='str')
bond =  pd.read_csv(data_path+'bonds/bond_dataset_jordan.csv',dtype='str')

#-----------------------------------------------------------------------------
# lecture specific variables: stcks
#-----------------------------------------------------------------------------
stck['next_ret'] = stck.rolling() 
stck['noshares'] = 1000.

# date 0 vars
stck['assets0'] = stck['noshares']*stck['price']
stck['margin0_usd'] = imr_act*stck['assets0']
stck['margin0_pct'] = imr_act
stck['liabilities0'] = stck['assets0']-stck['margin0_usd']

#-----------------------------------------------------------------------------
# lecture specific variables: bonds
#-----------------------------------------------------------------------------

# date 0 vars
stck['assets1'] = stck['noshares']*stck['price']*(1.+stck['next_ret'])
stck['liabilities1'] = (1.+interest_rate)*stck['liabilities0']
stck['margin1_usd'] = imr_act*stck['assets0']
stck['margin1_pct'] = 

# create problems
prob_file = open('asset_markets_problems','r')
problems = prob_file.read()
problems = problems[:-1].split('\n\n')

# loop over problems
for problem in problems:
    for j in range(0,n):

        # unpack problem
        temp, problem_code, data_set, Q, A = re.split(':: ',problem)
        this_port = stck.sample(1).to_dict('records')[0]
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
