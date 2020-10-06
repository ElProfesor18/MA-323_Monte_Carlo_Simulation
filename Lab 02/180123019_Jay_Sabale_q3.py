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
		res = 0.50 - 0.50*math.cos(math.pi*t)
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

# Plots y = (2/pi) arc sin(root(x))
def plotActualDistributionFunction():
	in_array = np.linspace(-1.00, 1.00, 10000) 
	out_array = np.arcsin(in_array) 
	  
	# print("in_array : ", in_array) 
	# print("\nout_arraywith arcsin : ", out_array) 
	  
	# red for numpy.arcsin() 
	plt.plot(in_array, out_array, 
	            color = 'blue', marker = "*") 
	              
	plt.title("Y = F(x)") 
	plt.xlabel("X") 
	plt.ylabel("Y") 
	plt.show() 

def execute(cnt):
	print("For input size of : " + str(cnt))
	u = getU(cnt) 
	u.sort()
	# print(u)
	x = getX(u)
	# print(x) 

	sMean, sVariance = getSampleMeanVariance(x)
	print("Sample Mean: " + str(sMean)) 
	print("Sample Variance: " + str(sVariance)) 
	print()
	plotCDF(x)

def main():
	plotActualDistributionFunction()

	execute(10)
	execute(100)
	execute(1000)
	execute(10000)
	execute(100000)

if __name__ == '__main__':
	main()






