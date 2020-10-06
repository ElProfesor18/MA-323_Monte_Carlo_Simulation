import matplotlib.pyplot as plt
import numpy as np   
import random

c = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Probabilities
p = [0.11, 0.12, 0.09, 0.08, 0.12, 0.10, 0.09, 0.09, 0.10, 0.10]
# Cumulative Probabilities
q = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
# Number of samples
sampleSize = [100, 1000, 10000, 100000, 1000000]

def upper_bound(arr, N, X):
	mid = 0
	low = 0 
	high = N
	while (low < high):
		mid = int((low + high)/2)
		if X >= arr[mid]:
			low = mid + 1
		else: 
			high = mid
		
	return low

def generate(_c):
	count = 0

	while True:
		count += 1
		curr = random.uniform(0.00, 1.00)
		key = upper_bound(q, len(q), curr)

		res = -1
		for j in range(max(key-5, 0), len(q)-1, 1):
			if curr>q[j]and curr<=q[j+1]:
				res = c[j]
				break

		u = np.random.uniform(0.00, 1.00)
		if u < p[res-1]/(_c*0.10):
			return res, count

def plotBarGraph(xAxis, yAxis): 
	fig = plt.figure(figsize = (10, 3)) 
	  
	# creating the bar plot 
	plt.bar(xAxis, yAxis, color ='blue',  
	        width = 0.75) 
	  
	plt.xlabel("Frequency Range") 
	plt.ylabel("") 
	plt.show()

def plotHistogram(res, _c, N):
	req = []
	for i in range(10):
		prob = p[i]
		total = int(N*prob)
		for j in range(total):
			req.append(i+1)

	plt.hist([res, req], bins=10)
	plt.title("For c = {} and sample size = {}.".format(_c, N)) 
	plt.xlabel('X')
	plt.ylabel('Probability')
	plt.show()
	plt.plot()


def plotGraphNormal(xAxis, yAxis, _c, N):
	plt.plot(xAxis, yAxis, label = "Sample Distribution")
	plt.plot(xAxis, p, label = "Required Distribution")

	# naming the x axis 
	plt.xlabel('Probability') 
	# naming the y axis 
	plt.ylabel('x')

	plt.legend(loc = "upper right")

	# giving a title to my graph 
	plt.title("For c = {} and sample size = {}.".format(_c, N)) 
	  
	# function to show the plot 
	plt.show()

def execute(_c, N):
	print("For c = {} and sample size = {}.".format(_c, N))
	iterations = []
	rand_sample = []
	for i in range(N):
		c, itr = generate(_c)
		rand_sample.append(c)
		iterations.append(itr)

	cntr = {}
	for i in range(10):
		cntr[i+1] = 0
	for i in rand_sample:
		cntr[i] += 1

	avg_iter = 0.00
	for i in iterations:
		avg_iter += i
	avg_iter = avg_iter/len(iterations)

	print("Average iterations required : {}.".format(avg_iter))

	xAxis = []
	yAxis = []
	res = []
	prob = []
	for i in range(10):
		print(str(i+1) + " " + str(cntr[i+1]) + " " + str(cntr[i+1]/N))
		yAxis.append(cntr[i+1]/N)
		xAxis.append(i+1)
		for j in range(cntr[i+1]):
			res.append(i+1)
		prob.append(cntr[i+1]/N)

	plotHistogram(res, _c, N)

def main():
	c1 = 1.50
	c2 = 2.00
	for i in sampleSize:
		execute(c1, i)
		execute(c2, i)
	

if __name__ == '__main__':
	main()



