import matplotlib.pyplot as plt

b = 51749
m = 244944
x0 = [1, 2, 3, 4, 5]

### Generates x_i's from given recurrence
def generateX(a, curr):
	x = []
	x.append(x0[curr]);
	for i in range (244944):
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

def generateData(u, curr):
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

def plotBarGraph(u, a, curr):
	# creating the dataset 
	data = generateData(u, curr)

	for key, val in data.items():
		print(str(val))
	print("\n\n\n")
	
	courses = list(data.keys()) 
	values = list(data.values()) 
	   
	fig = plt.figure(figsize = (10, 3)) 
	  
	# creating the bar plot 
	plt.bar(courses, values, color ='blue',  
	        width = 0.75) 
	  
	plt.xlabel("Frequency Range") 
	plt.ylabel("Frequency") 
	plt.title("q2 for x0 = " + str(x0[curr]) + " for a = " + str(a))
	plt.show() 

def main():
	a = 1597

	for curr in range(len(x0)):
		x = generateX(a, curr)
		ulist = generateU(x)

		plotBarGraph(ulist, a, curr)

	a = 51749

	for curr in range(len(x0)):
		x = generateX(a, curr)
		ulist = generateU(x)

		plotBarGraph(ulist, a, curr)



if __name__ == "__main__":
	main()





