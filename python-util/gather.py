import serial
import numpy as np
import matplotlib.pyplot as plt
import csv
import os
# change CWD to directory of script
os.chdir(os.path.dirname(__file__))
print(os.getcwd())

N = 10		# number of samples to collect
label_dict = {
	"lying": 0,
	"standing": 1,
	"walking": 2
}
DATA_PATH = "data/raw.csv"

def main():
	# open serial port
	port_name = 'COM3'
	try:
		ser = serial.Serial(port_name, 115200, timeout=5)
	except:
		print("Could not connect to port, exiting...")
		exit()

	# if data is not coming in, wait until the first line of data comes
	line = ser.readline()
	if len(line) <= 1:
		print("Data not available on serial port, exiting...")
		exit()

	print("Started reading COM port...")

	# collect N values of acc and gyro data and write to csv
	stream = []
	for i in range(N):
		line = ser.readline()
		vector = [float(d) for d in line.split(b',')]
		# print(vector)
		if len(vector) != 6:
			print("Data on serial port not in correct format, exiting...")
			exit()
		stream.append(vector)

	print("Finished serial read.")
	ser.close()

	stream = np.array(stream)
	# plot accx data for now
	# TODO: plot other signals in same plot with labels
	plt.plot(stream.T[0])
	plt.show()

	# assign label to data
	gotlabel = False
	while gotlabel is False:
		labelstr = input("Enter label for this datapoint: ")
		try:
			label = label_dict[labelstr]
			gotlabel = True
		except:
			print("Please enter label from the following only: ")
			print([k for k in label_dict.keys])

	# flatten all data values in a single row, with last element being the label
	row = np.append(stream.flatten(), [label])
	# print(row)

	# write to data.csv
	with open(DATA_PATH, 'w') as file:
		writer = csv.writer(file)
		writer.writerow(row)

	print("Done writing row to csv file, exiting...")


def normalise_stream(stream):
	# stream is Nx6 np array
	GYRO_NORM = 500	# max deg per sec sensed by imu
	ACCEL_NORM = 80	# imu accel set to +/- 8G
	# TODO: use advanced indexing instead of this shit

if __name__ == "__main__":
	main()