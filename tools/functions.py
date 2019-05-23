
import numpy as np
from math import cos,sqrt

def brownian(T):

    N = 8000

    dt = T/(N-1) # Time step

    # Preallocate arrays for efficiency:
    dX = [0]*N
    X = [0]*N

    # Initialization:
    dX[0] = np.sqrt(dt)*np.random.randn()
    X[0] = dX[0]

    for i in range(1,N):
        dX[i] = np.sqrt(dt)*np.random.randn()
        X[i] = X[i-1] + dX[i]

    return X

def weierstrass(step=0.0001):

    a = 0.73
    b = 5
    n = 100
    intervalBegin = 0
    intervalEnd = 1
    data = []
    for x in range(int((1 / step) * abs(intervalEnd - intervalBegin))):
        output = 0
        for i in range(n):
            output += pow(a, i) * cos(pow(b, i) * i * x * step)
        data.append(output)

    return data

def white(mu=0, variance=1, numPoints=2**13):

    sigma = math.sqrt(variance)
    data = np.random.normal(mu, sigma, size=numPoints)

    return data
