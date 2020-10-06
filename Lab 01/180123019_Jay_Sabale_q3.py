import matplotlib.pyplot as plt
a = 1229
b = 1
m = 2048
x0 = 3

x = []
ulist = []

xAxis = []
yAxis = []

### Generates x_i's from given recurrence
def generateX():
	x.append(x0)
	for i in range (2050):
		prev = x[len(x)-1]
		curr = (a*prev + b) % m
		x.append(curr)

### Generates u_i's from given recurrence
def generateU():
	for i in x:
		ulist.append(i/m)

### Generates Co-Ordinate lists to be plot.
def fillCoordinates():
	for i in range(len(ulist)-1):
		xAxis.append(ulist[i])
		yAxis.append(ulist[i+1])
	

def plotGraphNormal():
	plt.plot(xAxis, yAxis)

	# naming the x axis 
	plt.xlabel('u(i) - axis') 
	# naming the y axis 
	plt.ylabel('u(i-1) - axis')

	# giving a title to my graph 
	plt.title('q3') 
	  
	# function to show the plot 
	plt.show()

def plotGraphScattered():
	plt.scatter(xAxis, yAxis)

	# naming the x axis 
	plt.xlabel('u(i) - axis') 
	# naming the y axis 
	plt.ylabel('u(i-1) - axis')

	# giving a title to my graph 
	plt.title('q3') 
	  
	# function to show the plot 
	plt.show()

def main():
	generateX()
	generateU()

	fillCoordinates()
	plotGraphNormal()
	plotGraphScattered()


if __name__ == "__main__":
	main()


























