import numpy as np

def vandermonde(x):
    n = x.size
    V = np.zeros((n, n))
    for i in range(n):
        V[:, i] = x ** i
    return V
m = vandermonde(np.array([[1, 2, 3]]))
print(m)
