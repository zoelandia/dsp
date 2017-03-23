# Matrix Algebra

import numpy as np

A = np.matrix([[1,2,3],[2,7,4]])
B = np.matrix([[1,-1],[0,1]])
C = np.matrix([[5,-1],[9,1],[6,0]])
D = np.matrix([[3,-2,-1],[1,2,3]])

u = np.array([6,2,-3,5])
v = np.array([3,5,-1,4])
w = np.array([[1],[8],[0],[5]])

# Matrix Dimensions
print(np.shape(A))          #1.1
print(np.shape(B))          #1.2
print(np.shape(C))          #1.3
print(np.shape(D))          #1.4
print(np.shape(u))          #1.5    returns (4), but really as a vector it's 1-dimensional
print(np.shape(w))          #1.6    returns (4,1), but same deal


# Vector operations
alpha = 6
print(u + v)                #2.1
print(u - v)                #2.2
print(alpha * u)            #2.3
print(np.dot(u, v))         #2.4
print(np.linalg.norm(u))    #2.5

# Matrix operations
A_t = np.transpose(A)
C_t = np.transpose(C)
#print(A + C)               #3.1    not defined
print(A - C_t)              #3.2
print(C_t + 3 * D)          #3.3
print(B * A)                #3.4
#print(B * A_t)             #3.5    not defined

# Optional
D_t = np.transpose(D)
#print(B * C)               #3.6    not defined
print(C * B)                #3.7
print(B**4)                 #3.8
print(A * A_t)              #3.9
print(D_t * D)              #3.10
