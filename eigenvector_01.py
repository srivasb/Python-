#Programa que resuelve problema de autovalores de A

import numpy as np

A = np.array([[-2,2,-3],[2,1,-6],[-1,-2,0]])

print(A)

x = np.linalg.eigvals(A)

print(x)
