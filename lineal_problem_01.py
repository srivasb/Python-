

import numpy as np

A = np.array([[0.18,0.60,0.57,0.96],[0.41,0.24,0.99,0.58],[0.14,0.30,0.97,0.66],[0.51,0.13,0.19,0.85]])

print(A)

b = np.array([1.0,2.0,3.0,4.0])

print(b)

x =np.linalg.solve(A,b)
print(x)
