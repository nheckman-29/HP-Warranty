#HP Warranty Retrieval - Nathan Heckman
#Works off of 'All Systems' report from SCCM

import pandas as p
import os as os

#Change directory to where the CSV file is or navigate in shell where Python is running
#os.chdir(PATH)

file = p.read_csv('all_systems.csv')

