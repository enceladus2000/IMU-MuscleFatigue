import csv
import numpy as np
import os
# change CWD to directory of script
os.chdir(os.path.dirname(__file__))
print(os.getcwd())

RAW_DATA_PATH = "data/raw.csv"
AUGMENT_DATA_PATH = "data/augmented.csv"

"""
1. rotate
2. amp/reduce
3. stretch+randomtrans
4. translate+pad
5. white noise
"""

# for now, only (2) and (5)

# open raw.csv
with open(RAW_DATA_PATH, 'r', newline='') as inp, open(AUGMENT_DATA_PATH, 'w', newline=''):
	# for every csv row, extract label and 100x6 feature matrix
	reader = csv.reader(inp)
	for row in reader:
		# amp = 
# generate random 1x9 amp vector within specified range
# multiply with all 100 vectors in feature matrix
# make white noise matrix and add to feature matrix
# write modified row to output file