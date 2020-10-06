import matplotlib.pyplot as plt
import numpy as np   
import random

# Smallest constant c1 that satisfies the
# inequality f(x)<=c1.g(x)
c1 = 2.1094
c2 = 2.5
c3 = 3.0
# Number of samples
sampleSize = [100, 1000, 10000, 100000, 1000000]

def f(x):
	return 20.00*x*((1-x)**3.00)

def plotHistogram(rand_sample, c, N):
	hist, bins, _ = plt.hist(rand_sample, density=True, bins=100)
	xAxis = (bins[1:]+bins[:-1])/2
	yAxis = 20.00*xAxis*((1-xAxis)**3.00)

	plt.plot(xAxis, yAxis, label = "f(x)")
	plt.legend(loc = "upper right")
	plt.xlabel('x')
	plt.ylabel('y')
	plt.title('c = ' + str(c) + ' samples = ' + str(N))

	plt.show()

def generate(c):
	count = 0
	while True:
		count += 1
		x = np.random.uniform(0.00, 1.00)
		u = np.random.uniform(0.00, 1.00)
		# g(x) = 1 for U[0.00, 1.00]
		if u <= f(x)/c:
			return x, count

def findAverage(rand_sample, iterations):
	avg_rand = 0.00
	avg_itr = 0.00
	
	for i in rand_sample:
		avg_rand += i
	avg_rand /= len(rand_sample)

	for i in iterations:
		avg_itr += i
	avg_itr /= len(iterations)

	return avg_rand, avg_itr

def execute(curr, N):
	c = curr
	iterations = []
	rand_sample = []
	for i in range(N):
		x, itr = generate(c)
		rand_sample.append(x)
		iterations.append(itr)

	avg_rand, avg_itr = findAverage(rand_sample, iterations)

	print('For c = ' + str(c) +' and sample size = ' + str(N) + ' : ', end = ' ')
	print('|c - avg_itr| = ' + str(abs(c-avg_itr)))

	if c == 2.1094:
		plotHistogram(rand_sample, c, N)

def main():
	for i in sampleSize:
		N = i
		execute(c1, N)

	for i in sampleSize:
		N = i
		execute(c2, N)

	for i in sampleSize:
		N = i
		execute(c3, N)
	

if __name__ == "__main__":
	main()































