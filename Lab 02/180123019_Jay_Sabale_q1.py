import matplotlib.pyplot as plt
a = 1229
b = 1
m = 2048
x0 = 3

### Generates x_i's from given recurrence
def generateX():
	x = []
	x.append(x0)
	for i in range (16):
		prev = x[len(x)-1]
		curr = (a*prev + b) % m
		x.append(curr)

	return x

### Generates u_i's from given recurrence
def generateU(x):
	ulist = []
	for i in x:
		ulist.append(i/m)
	return ulist

def generateK(u, k):
	curr = 18
	while len(u)<k :
		key = u[curr-17] - u[curr-5]
		if key<0:
			key += 1.00
		u.append(key)
		curr += 1

def fillCoordinates(ulist):
	xAxis = []
	yAxis = []
	for i in range(len(ulist)-1):
		xAxis.append(ulist[i])
		yAxis.append(ulist[i+1])

	return xAxis, yAxis
	

def plotGraphNormal(u, xAxis, yAxis):
	plt.plot(xAxis, yAxis)

	# naming the x axis 
	plt.xlabel('u(i+1) - axis') 
	# naming the y axis 
	plt.ylabel('u(i) - axis')

	# giving a title to my graph 
	plt.title('q1: Normal for ' + str(len(u)) + " values") 
	  
	# function to show the plot 
	plt.show()

def plotGraphScattered(u, xAxis, yAxis):
	plt.scatter(xAxis, yAxis)

	# naming the x axis 
	plt.xlabel('u(i+1) - axis') 
	# naming the y axis 
	plt.ylabel('u(i) - axis')

	# giving a title to my graph 
	plt.title('q1: Scattered for ' + str(len(u)) + " values") 
	  
	# function to show the plot 
	plt.show()

def generateData(u):
	data = {}
	data["0.00"] = 0
	data["0.05"] = 0
	data["0.10"] = 0
	data["0.15"] = 0
	data["0.20"] = 0
	data["0.25"] = 0
	data["0.30"] = 0
	data["0.35"] = 0
	data["0.40"] = 0
	data["0.45"] = 0
	data["0.50"] = 0
	data["0.55"] = 0
	data["0.60"] = 0
	data["0.65"] = 0
	data["0.70"] = 0
	data["0.75"] = 0
	data["0.80"] = 0
	data["0.85"] = 0
	data["0.90"] = 0
	data["0.95"] = 0
	data["1.00"] = 0

	for i in u:
		if i>=0.00 and i<0.05:
			data["0.00"] += 1

		elif i>=0.05 and i<0.10:
			data["0.05"] += 1

		elif i>=0.10 and i<0.15:
			data["0.10"] += 1
		
		elif i>=0.15 and i<0.20:
			data["0.15"] += 1
		
		elif i>=0.20 and i<0.25:
			data["0.20"] += 1
		
		elif i>=0.25 and i<0.30:
			data["0.25"] += 1
		
		elif i>=0.30 and i<0.35:
			data["0.30"] += 1
		
		elif i>=0.35 and i<0.40:
			data["0.35"] += 1
		
		elif i>=0.40 and i<0.45:
			data["0.40"] += 1 
		
		elif i>=0.45 and i<0.50:
			data["0.45"] += 1
		
		elif i>=0.50 and i<0.55:
			data["0.50"] += 1
		
		elif i>=0.55 and i<0.60:
			data["0.55"] += 1
		
		elif i>=0.60 and i<0.65:
			data["0.60"] += 1
		
		elif i>=0.65 and i<0.70:
			data["0.65"] += 1
		
		elif i>=0.70 and i<0.75:
			data["0.70"] += 1
		
		elif i>=0.75 and i<0.80:
			data["0.75"] += 1
		
		elif i>=0.80 and i<0.85:
			data["0.80"] += 1
		
		elif i>=0.85 and i<0.90:
			data["0.85"] += 1
		
		elif i>=0.90 and i<0.95:
			data["0.90"] += 1
		
		elif i>=0.95 and i<1.00:
			data["0.95"] += 1
		
		elif i>=1.00 and i<1.05:
			data["1.00"] += 1

	return data

def plotBarGraph(u, k):
	# creating the dataset 
	data = generateData(u)

	# for key, val in data.items():
	# 	print(str(val))
	# print("\n\n\n")
	
	courses = list(data.keys()) 
	values = list(data.values()) 
	   
	fig = plt.figure(figsize = (10, 3)) 
	  
	# creating the bar plot 
	plt.bar(courses, values, color ='blue',  
	        width = 0.75) 
	  
	plt.xlabel("Frequency Range") 
	plt.ylabel("Frequency") 
	plt.title("q1 for " + str(k) + " values") 
	plt.show() 

def main():
	x = generateX()
	u = generateU(x)

	print("The first 17 elements of the sequence Ui are : ")
	cnt = 0
	for i in u:
		print("U("+str(cnt)+") "+str(i))
		cnt+=1

	### ui corresponds to the first 1000, 10000 
	### and 100000 elements of the sequence U for i = 1, 2 and 3
	### respectively
	u1 = generateU(x)
	u2 = generateU(x)
	u3 = generateU(x)

	generateK(u1, 1000)
	generateK(u2, 10000)
	generateK(u3, 100000)

	x1, y1 = fillCoordinates(u1)
	x2, y2 = fillCoordinates(u2)
	x3, y3 = fillCoordinates(u3)

	# plotGraphNormal(u1, x1, y1)
	# plotGraphNormal(u2, x2, y2)
	# plotGraphNormal(u3, x3, y3)

	plotGraphScattered(u1, x1, y1)
	plotGraphScattered(u2, x2, y2)
	plotGraphScattered(u3, x3, y3)

	plotBarGraph(u1, 1000)
	plotBarGraph(u2, 10000)
	plotBarGraph(u3, 100000)


if __name__ == "__main__":
	main()
