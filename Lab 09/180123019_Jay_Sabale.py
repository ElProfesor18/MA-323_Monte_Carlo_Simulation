import pandas as pd
import numpy as np
import statistics
import math
import matplotlib.pyplot as plt

df = pd.read_csv('sbi_data.csv', usecols = ['Date', 'Close'], nrows = 66)


U = []
for i in range(65):
    U.append( math.log(df.Close[i+1]/df.Close[i]))

variance = statistics.variance(U)
sigma = math.sqrt(variance)
print(variance, sigma)

mean = statistics.mean(U)
print(mean)

mu = variance/2 + mean
print(mu)

S = []

data = []
for i in range(1000):
    data.append(0.00)

N = 1000
asian = []
european = []
for ctr in range(N):
    S.clear()
    S.append(df.Close[65])
    
    for i in range(1, 300):
        S.append(S[i-1]*math.exp((mu - variance/2.00)*0.1 + np.sqrt(variance)*np.sqrt(0.1)*np.random.normal(0,1,1)))
    
    for j in range(len(S)):
        data[j] += S[j]
        
    european.append(max(0, 1.1*S[0] - S[-1]))
    asian.append(max(1.1*S[0] - statistics.mean(S), 0))
    
# print("Mean European = {}, S.D European = {}".format(statistics.mean(european), np.sqrt(statistics.variance(european))))

print("Mean Asian = {}, S.D Asian = {}".format(statistics.mean(asian), np.sqrt(statistics.variance(asian))))

while data[-1] == 0.00:
    data.pop()
    
for j in range(len(data)):
    data[j] /= N

b = 0.00
for i in range(len(asian)):
    b = b + (asian[i] - statistics.mean(asian))*(european[i] - statistics.mean(european))/(1000*statistics.variance(european))

for i in range(len(asian)):
    asian[i] = asian[i] - b*(european[i] - statistics.mean(european))

print("Mean Asian = {}, S.D Asian = {}".format(statistics.mean(asian), np.sqrt(statistics.variance(asian))))
