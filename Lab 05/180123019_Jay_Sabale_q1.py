import matplotlib.pyplot as plt 
import numpy as np
from scipy.stats import norm
import math
import time

def getSampleMeanVariance(sample):
	sum = 0.00
	N = len(sample)
	for i in sample:
		sum += i

	avg = sum/(N)

	cnt = 0.00
	for i in sample:
		cnt += (i-avg)**2

	variance = cnt/(N-1)
	return avg, variance

def mean_variance(sample, type, N):
	if type == 0:
		print("For N(0, 1), ")

	if type == 1:
		print("For N(0, 5), ")

	if type == 2:
		print("For N(5, 5), ")

	sampleX = []
	sampleY = []

	for x, y in sample:
		sampleX.append(x)
		sampleY.append(y)

	m1, v1 = getSampleMeanVariance(sampleX)
	m2, v2 = getSampleMeanVariance(sampleY)

	print('Mean of {} numbers of z1 is {}'.format(N, m1))
	print('Mean of {} numbers of z2 is {}'.format(N, m2))

	print('Variance of {} numbers of z1 is {}'.format(N, v1))
	print('Variance of {} numbers of z2 is {}'.format(N, v2))

def boxMuller():
	u1 = np.random.uniform(0.00, 1.00)
	u2 = np.random.uniform(0.00, 1.00)

	R = -2.00*math.log(u1)
	V = 2.00*math.pi*u2

	Z1 = math.sqrt(R)*math.cos(V)
	Z2 = math.sqrt(R)*math.sin(V)

	return Z1, Z2

def marsgliaBray():
	X = 100.00
	u1 = 1.00
	u2 = 1.00

	rejected = 0
	total = 0
	while X > 1.00 :
		u1 = np.random.uniform(0.00, 1.00)
		u2 = np.random.uniform(0.00, 1.00)
		
		u1 = 2*u1 - 1.00
		u2 = 2*u2 - 1.00

		X = u1**2 + u2**2
		rejected += 1
		total += 1

	rejected -= 1
	Y = math.sqrt( (-2.00*math.log(X)) / X)
	Z1 = u1*Y
	Z2 = u2*Y

	return Z1, Z2, rejected, total

def plotCDF(sample, N, method):
	for i in range(N):
		sample[i][0] *= math.sqrt(5)
		sample[i][1] *= math.sqrt(5)

	data = []
	for x, y in sample:
		data.append(x)
		data.append(y)

	data_size = len(data)

	data_set = sorted(set(data))
	bins = np.append(data_set, data_set[-1]+1)

	counts, bin_edges = np.histogram(data, bins=bins, density=False)
	counts = counts.astype(float)/data_size
	cdf = np.cumsum(counts)

	# Mean = 0, Variance = 5, Color = Blue
	plt.plot(bin_edges[0:-1], cdf, linestyle='--', marker='o', color='m')
	plt.ylim((0, 1))
	plt.ylabel("CDF")
	plt.xlabel("x")
	plt.grid(True)

	for i in range(N):
		sample[i][0] += 5
		sample[i][1] += 5

	data = []
	for x, y in sample:
		data.append(x)
		data.append(y)

	data_size = len(data)

	data_set = sorted(set(data))
	bins = np.append(data_set, data_set[-1]+1)

	counts, bin_edges = np.histogram(data, bins=bins, density=False)
	counts = counts.astype(float)/data_size
	cdf = np.cumsum(counts)

	# Mean = 5, Variance = 5, Color = Red
	plt.plot(bin_edges[0:-1], cdf, linestyle='--', marker='o', color='c')
	plt.legend(["N(0, 5)", "N(5, 5)"])
	plt.ylim((0, 1))
	plt.ylabel("CDF")
	plt.grid(True)

	plt.title("For N = {}, Method = {}".format(N, method))

	plt.show()

def plotHistogram(sample, N,  method):
	print()
	data = []
	for x, y in sample:
		data.append(x)
		data.append(y)

	mean = 0
	variance = 1
	# Plot between -10 and 10 with .001 steps.
	x_axis = np.arange(-5, 5, 0.001)
	plt.plot(x_axis, norm.pdf(x_axis, mean, math.sqrt(variance)), color='m')

	hist, bins, _ = plt.hist(data, density=True, bins=100, color='c')
	plt.xlabel('x')
	plt.ylabel('y')
	plt.legend(['Actual Distribution for N(0, 1)'], loc = "upper right")

	plt.title('Frequency v/s Sample for N = {}, Method = {}'.format(N, method))
	plt.show()

def execute(N):
	sample_1 = []
	sample_2 = []
	rejected = 0
	total = 0

	# For N(0, 1)
	time_start = time.process_time_ns()
	for i in range(N):
		x, y = boxMuller()
		sample_1.append([x, y])
	tBoxMuller = (time.process_time_ns() - time_start)

	time_start = time.process_time_ns()
	for i in range(N):
		x, y, r, t = marsgliaBray()
		rejected += r
		total += t
		sample_2.append([x, y])
	tMarsgliaBray = (time.process_time_ns() - time_start)

	plotHistogram(sample_1, N, "Box-Muller")
	plotHistogram(sample_2, N, "Marsglia and Bray" )

	print('Box-Muller method: ')
	mean_variance(sample_1, 0, N)
	print()

	print('Marsglia and Bray method: ')
	mean_variance(sample_2, 0, N)
	print()

	plotCDF(sample_1, N, "Box-Muller")
	plotCDF(sample_2, N, "Marsglia and Bray")

	# Output Handling
	print("Time for Box-Muller (N = {}) {} ns".format(N, tBoxMuller))
	print("Time for Marsglia and Bray (N = {}) {} ns".format(N, tMarsgliaBray))
	print()

	print("{} {}".format(rejected, total))
	print("For N = {}, Required Comparison = {}".format(N, abs(1-math.pi/4 - rejected/total)))

	print("\n\n")

def main():
	execute(100)
	execute(10000)

if __name__ == '__main__':
	main()










