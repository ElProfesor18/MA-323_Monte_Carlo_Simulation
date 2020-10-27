import pandas as pd
import numpy as np
import statistics
import math
import matplotlib.pyplot as plt

df = pd.read_csv('sbi_data.csv', usecols = ['Date', 'Close'], nrows = 66)


U = []
for i in range(65):
    U.append( math.log(df.Close[i+1]/df.Close[i]) )

variance = statistics.variance(U)
sigma = math.sqrt(variance)
print(variance, sigma)

mean = statistics.mean(U)
print(mean)

mu = variance/2 + mean
print(mu)

S = []

# t1 -> t(i)
# t2 -> t(i+1)
def predict(t1, t2):
    S[t2] = S[t1] * math.exp( (mu-variance/2)*(t2-t1) + sigma * math.sqrt((t2-t1)) * np.random.normal(0.00, 1.00))
    return S[t2]

# 7th of October is Day Number 5 (Day 69 in CSV)
# 14th of October is Day Number 10 (Day 74 in CSV)
# 21st of October is Day Number 15 (Day 79 in CSV)
# *** Saturday - Sundays are off***

data = []
for i in range(100000):
    data.append(0.00)

N = 1000
for ctr in range(N):
    S.clear()
    S.append(df.Close[65])
    
    for i in range(1, 16):
        S.append(S[i-1]*math.exp(mean + np.sqrt(variance)*np.random.normal(0,1,1)))
    
    for j in range(len(S)):
        data[j] += S[j]

while data[-1] == 0.00:
    data.pop()
    
for j in range(len(data)):
    data[j] /= N


df = pd.read_csv('sbi_data.csv', usecols = ['Date', 'Close'])

key = []
for i in range(65):
    key.append(df.Close[i])

for i in data:
    key.append(i)
    
predicted = pd.Series(key)

df['Predicted_Close'] = predicted

df['Error %'] = ((abs(df['Predicted_Close'] - df['Close']))/df['Close'])*100


df.to_csv('180123019_Jay_Sabale_Prediction.csv')