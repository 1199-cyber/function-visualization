import numpy as np

def linear(x, a=1, b=0):
    return a * x + b

def quadratic(x, a=1, b=0, c=0):
    return a * x**2 + b * x + c

def sine(x, a=1):
    return np.sin(a * x)

def cosine(x, a=1):
    return np.cos(a * x)

def exponential(x, a=1):
    return np.exp(a * x)

def cubic(x):
    return x**3
