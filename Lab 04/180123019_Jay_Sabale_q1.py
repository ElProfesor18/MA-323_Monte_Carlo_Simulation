import matplotlib.pyplot as plt 
from scipy.special import gamma
import numpy as np

# Plots Histogram along side acutal distribution
def plotHistogram(sample, a1, a2, N):
	hist, bins, _ = plt.hist(sample, density=True, bins=100)
	xAxis = (bins[1:]+bins[:-1])/2
	yAxis = []
	for x in xAxis:
		yAxis.append(fx(x, a1, a2))

	plt.plot(xAxis, yAxis, label = "f(x)")
	plt.legend(loc = "upper right")
	plt.xlabel('x')
	plt.ylabel('y')
	plt.show()

# Computes f(x)
def fx(x, a1, a2):
	res = (x**(a1-1))*((1-x)**(a2-1))
	res /= beta(a1, a2)
	return res

# Computes B(a1, a2)
def beta(a1, a2):
	res = (gamma(a1)*gamma(a2))/(gamma(a1+a2))
	return res

# Generates Beta Distribution of N values
def generateBeta(a1, a2, c, N):
	res = []
	for i in range(N):
		while True:
			u1 = np.random.uniform(0.00, 1.00)
			u2 = np.random.uniform(0.00, 1.00)

			if fx(u1, a1, a2) >= c*u2:
				res.append(u1)
				break

	return res

def solve(a1, a2):
	x = (a1-1)/(a1+a2-2)
	print('*x = {}'.format(x))
	c = fx(x, a1, a2)
	print('f(*x) = {}'.format(c))

	res = generateBeta(a1, a2, c, 100)
	plotHistogram(res, a1, a2, 100)
	
	res = generateBeta(a1, a2, c, 1000)
	plotHistogram(res, a1, a2, 1000)
	
	res = generateBeta(a1, a2, c, 10000)
	plotHistogram(res, a1, a2, 10000)
	
	res = generateBeta(a1, a2, c, 100000)
	plotHistogram(res, a1, a2, 100000)
	
	# res = generateBeta(a1, a2, c, 1000000)
	# plotHistogram(res, a1, a2, 1000000)
	

def main():
	solve(1.43, 2.76)
	# solve(1.25, 2.0)
	# solve(1.25, 2.75)
	# solve(1.0, 2.0)
	# solve(3.25, 4.75)
	# solve(2.25, 1.75)

if __name__ == '__main__':
	main()