from numpy import random
import numpy as np
import matplotlib.pyplot as plt
import math

### Defining theta
theta = math.pi/4

### Generates count number of random values in the range [0, 1]
def getU(count):
	u = []
	for i in range(count):
		key = random.rand()
		u.append(key)

	return u

def getX(u):
	x = []
	for t in u:
		res = -theta*(math.log(1-t))
		x.append(res)
	
	return x

def getSampleMeanVariance(x):
	sum = 0.00
	for i in x:
		sum += i

	avg = sum/(len(x))

	cnt = 0.00
	for i in x:
		cnt += (i-avg)**2

	variance = cnt/(len(x)-1)
	return avg, variance

def plotCDF(data):
	data_size = len(data)

	data_set = sorted(set(data))
	bins = np.append(data_set, data_set[-1]+1)

	counts, bin_edges = np.histogram(data, bins=bins, density=False)

	counts = counts.astype(float)/data_size

	cdf = np.cumsum(counts)

	plt.plot(bin_edges[0:-1], cdf, linestyle='--', marker='o', color='b')
	plt.ylim((0, 1))
	plt.ylabel("CDF")
	plt.grid(True)

	plt.show()
	

# Plots y = 1 - e^(-x/theta)
def plotActualDistributionFunction():
	a = -1
	b = 1/theta
	c = 1
	x = np.linspace(0, 10, 256, endpoint = True)
	y = (a * np.exp(-b*x)) + c

	plt.plot(x, y, '-r', label=r'$y =  1 - e^{-x/theta}$')

	axes = plt.gca()
	axes.set_xlim([x.min(), x.max()])
	axes.set_ylim([y.min(), y.max()])

	plt.xlabel('x')
	plt.ylabel('y')
	plt.title('Actual Distribution')
	plt.legend(loc='upper left')

	plt.show()

def execute(cnt):
	print("For input size of : " + str(cnt))
	u = getU(cnt) 
	u.sort()
	# print(u)
	x = getX(u)
	# print(x) 

	sMean, sVariance = getSampleMeanVariance(x)
	# Actual Mean is theta
	print("Sample Mean: " + str(sMean) + " "  + "Actual Mean: " + str(theta)) 
	print("Abs. Difference : " + str(abs(sMean-theta)))
	# Actual Variance is theta^2
	print("Sample Variance: " + str(sVariance) + " " + "Actual Variance: " + str(theta**2)) 
	print("Abs. Difference : " + str(abs(sVariance-theta**2)))
	print()

	plotCDF(x)

def main():
	plotActualDistributionFunction()

	execute(10)
	execute(100)
	execute(1000)
	execute(10000)
	execute(100000)
	# execute(1000000)

if __name__ == '__main__':
	main()






