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
print(np.shape(A))          #1.1    (2, 3)
print(np.shape(B))          #1.2    (2, 2)
print(np.shape(C))          #1.3    (3, 2)
print(np.shape(D))          #1.4    (2, 3)
print(np.shape(u))          #1.5    returns (4), but really as a vector it's 1-dimensional
print(np.shape(w))          #1.6    returns (4, 1), but same deal


# Vector operations
alpha = 6
print(u + v)                #2.1    [9 7 -4 9]
print(u - v)                #2.2    [3 -3 -2 1]
print(alpha * u)            #2.3    [36 12 -18 30]
print(np.dot(u, v))         #2.4    [51]
print(np.linalg.norm(u))    #2.5    [sqrt(74), or ~8.60]

# Matrix operations
A_t = np.transpose(A)
C_t = np.transpose(C)
#print(A + C)               #3.1    not defined
print(A - C_t)              #3.2    [[-4 -7 -3], [3 6 4]]
print(C_t + 3 * D)          #3.3    [[14 3 3], [2 7 9]]
print(B * A)                #3.4    [[-1 -5 -1], [2 7 4]]
#print(B * A_t)             #3.5    not defined

# Optional
D_t = np.transpose(D)
#print(B * C)               #3.6    not defined
print(C * B)                #3.7    [[5 -6], [9 -8], [6 -6]]
print(B**4)                 #3.8    [[1 -4], [0 1]]
print(A * A_t)              #3.9    [[14 28], [28 69]]
print(D_t * D)              #3.10   [[10 -4 0], [-4 8 8], [0 8 10]]
