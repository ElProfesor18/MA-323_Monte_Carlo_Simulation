import math
import pandas as pd
import numpy as np
import statistics
import matplotlib.pyplot as plt

a = 51749
b = 1352
m = 244944
x0 = 3

# Plots Histogram along side acutal distribution
def plotHistogram(sample, method):
    hist, bins, _ = plt.hist(sample, density=True, bins=100)
    
    plt.title('Sample Distribution for N = {}, {}'.format(len(sample), method))
    plt.show()


### Generates x_i's from given recurrence
def generateX(a, curr, N):
    x = []
    x.append(curr);
    for i in range (N-1):
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

def LCG(N):
    curr = 3
    x = generateX(a, curr, N)
    ulist = generateU(x)

    plotHistogram(ulist, 'Linear Congruence Generator')

def generateVC(N):
    data = [i for i in range(N)]
    
    sample = []
    for t in data:
        binary = []
        n = t

        if n==0:
            binary.append(0)

        while n!=0:
            bit = n%2
            binary.append(bit)
            n = n//2

        curr = 0.00
        temp = 1.00/2.00
        for mult in binary:
            curr += mult*temp
            temp = temp/2

        sample.append(curr)

    df = pd.DataFrame()
    df['N'] = pd.Series([i for i in range(N)])
    df['Van der Corput(N)'] = pd.Series(sample)

    return df


def generateHalton(N):
    data = [i for i in range(N)]
    
    sampleX = []
    sampleY = []
    for t in data:
        binary = []
        ternary = []
        
        n = t
        if n==0:
            binary.append(0)

        while n!=0:
            bit = n%2
            binary.append(bit)
            n = n//2
        
        n = t
        if n==0:
            ternary.append(0)

        while n!=0:
            bit = n%3
            ternary.append(bit)
            n = n//3

        curr = 0.00
        temp = 1.00/2.00
        for mult in binary:
            curr += mult*temp
            temp = temp/2.00
        phi_2 = curr
        
        curr = 0.00
        temp = 1.00/3.00
        for mult in binary:
            curr += mult*temp
            temp = temp/3.00
        phi_3 = curr
        
        sampleX.append(phi_2)
        sampleY.append(phi_3)

    return sampleX, sampleY

def partA():
    df1 = generateVC(25)
    df2 = generateVC(1000)

    print("The first 25 values of the Van der Corput sequence are: ")
    print(df1)

    xAxis = []
    yAxis = []

    for i in range(len(df2['Van der Corput(N)'])-1):
        xAxis.append(df2['Van der Corput(N)'][i])
        yAxis.append(df2['Van der Corput(N)'][i+1])

    plt.plot(xAxis, yAxis)
    plt.xlabel('x(i)')
    plt.ylabel('x(i+1)')
    plt.show()

    df3 = generateVC(100)
    plotHistogram(df3['Van der Corput(N)'], 'Van der Corput')
    LCG(100)

    df4 = generateVC(100000)
    plotHistogram(df4['Van der Corput(N)'], 'Van der Corput')
    LCG(100000)


def partB():
    H_sample_X, H_sample_Y = generateHalton(10000)

    plt.plot(H_sample_X, H_sample_Y)
    plt.title('Halton Sequence Actual')
    plt.xlabel('phi_2(i)')
    plt.ylabel('phi_3(i)')
    plt.show()

    plt.scatter(H_sample_X, H_sample_Y)
    plt.title('Halton Sequence Scattered')
    plt.xlabel('phi_2(i)')
    plt.ylabel('phi_3(i)')
    plt.show()


def main():
    partA()
    partB()


if __name__ == '__main__':
    main()




