import csv
import numpy as np
import os
# change CWD to directory of script
os.chdir(os.path.dirname(__file__))
print(os.getcwd())
# TODO: revise noise values! 

RAW_DATA_PATH = "data/raw.csv"
AUGMENT_DATA_PATH = "data/augmented.csv"
num_samples = 100
"""
1. rotate
2. amp/reduce
3. stretch+randomtrans
4. translate+pad
5. white noise
"""
# augmentation transform parameters
augment_multiplier = 3			# factor by which to increase volume of data
amp_accel_range = [0.95, 1.05]
amp_gyro_range = [0.9, 1.1]
noise_accel = [0.05, 0.05]		# first val is std, 2nd is multiplier aka level
noise_gyro = [.01, .01]

# for now, only (2) and (5)

def main():
	# open raw.csv
	with open(RAW_DATA_PATH, 'r', newline='') as inp, open(AUGMENT_DATA_PATH, 'w', newline='') as out:
		reader = csv.reader(inp)
		writer = csv.writer(out)

		for row in reader:
			for i in range(augment_multiplier):
				# first row should be same as raw
				if i == 0:
					writer.writerow(row)
					continue
				# other rows should be transformed
				label, fmat = get_contents(row)

				# amplify by random amp vec
				fmat = add_random_amp(fmat, amp_accel_range, amp_gyro_range)
				# add white noise
				fmat = add_whitenoise(fmat, noise_accel, noise_gyro)
				# append to output file
				fmat = np.append([label], fmat.flatten())
				writer.writerow(fmat)

def get_contents(row):
	label = row[0]
	fmat = row[1:]
	fmat = np.array(fmat).reshape((num_samples, 6)).astype(np.float32)
	return label, fmat

def add_whitenoise(fmat, noise_accel, noise_gyro):
	accelmat = noise_accel[1] * np.random.normal(scale=noise_accel[0], size=(num_samples, 3))
	gyromat = noise_gyro[1] * np.random.normal(scale=noise_gyro[0], size=(num_samples, 3))

	return fmat + np.append(accelmat, gyromat, axis=1)

def add_random_amp(fmat, accel_range, gyro_range):
	accel_vec = accel_range[0] + (accel_range[1] - accel_range[0]) * np.random.rand(3)
	gyro_vec = gyro_range[0] + (gyro_range[1] - gyro_range[0]) * np.random.rand(3)
	amp = np.append(accel_vec, gyro_vec)
	return amp * fmat

if __name__ == '__main__':
	main()