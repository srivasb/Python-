#Programa que calcula la inversa de una matriz A:
#A*inv(A)=1

import numpy as np

A = np.array([[4.0,-2.0,1.0],
              [3.0,6.0,-4.0],
              [ 2.0,1.0,8.0]])

print(A)

x = np.linalg.inv(A)

print(x)

#result = [[sum(a*b for a,b in zip(X_row,Y_col)) for Y_col in zip(*x)] for X_row in A]


p = x * A
d = A * x

print(p)
print(d)


