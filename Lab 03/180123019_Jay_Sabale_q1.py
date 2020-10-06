import matplotlib.pyplot as plt
import numpy as np   
import random

# Number of samples
sampleSize = [100, 1000, 10000, 100000, 1000000]
MAXN = 9999

### Generates the sequence 1, 3, 5, ... 9999
def generateC():
	c = []
	curr = 1
	while curr<=MAXN:
		c.append(curr)
		curr += 2

	return c

### Generates first k terms of the sequence Ui
### All ui are uniform in range [0, 1]
def generateK(k):
	u = []
	for i in range(k):
		u.append(np.random.uniform(0.00, 1.00))
	return u

def generateQ(c):
	q = []
	key = 1/len(c)
	curr = 0
	while curr<1.00:
		q.append(curr)
		curr += key
	q.append(curr)

	return q

def plotBarGraph(xAxis, yAxis): 
	fig = plt.figure(figsize = (10, 3)) 
	  
	# creating the bar plot 
	plt.bar(xAxis, yAxis, color ='blue',  
	        width = 0.75) 
	  
	plt.xlabel("Frequency Range") 
	plt.ylabel("") 
	plt.show()

def plotHistogram(N, res):
	plt.hist(res, bins = 100)
	plt.title("For sample size of N = " + str(N))
	plt.xlabel('X')
	plt.ylabel('Frequency')
	plt.show()

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

def execute(c, q, N):
	u = generateK(N)

	res = []
	for i in u:
		curr = i
		key = upper_bound(q, len(q), curr)
		
		for j in range(max(key-5, 0), len(q)-1, 1):
			if curr>q[j]and curr<=q[j+1]:
				res.append(c[j])
				break

	res.sort()

	data = {}
	for i in c:
		data[i] = 0

	for i in res:
		data[i] += 1

	xAxis = []
	yAxis = []
	for i in c:
		xAxis.append(i)
		yAxis.append(data[i])

	cntr = {}
	for i in range(10001):
		cntr[i] = 0

	# for i in res:
	# 	cntr[i] += 1

	# for i in range(1, 10000, 2):
	# 	print(str(i) + ' ' + str(cntr[i]/N))

	# plotBarGraph(xAxis, yAxis)
	plotHistogram(N, res)

def main():
	# Generates the sequence ci: 1, 3, 5 ... 9999
	c = generateC()
	# Generates prefix sum of resulting probabilties!
	q = generateQ(c)
	
	for i in sampleSize:
		execute(c, q, i)

if __name__ == "__main__":
	main()
