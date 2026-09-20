import Matrix as M
import numpy as np
import timeit as t
import matplotlib.pyplot as plt

# matrix1 = M.Matrix([[1,2,-1], [2,1,2], [-1,2,1]])
# matrix2 = M.Matrix([[1,1,0], [1,1,0], [1,1,1]])

# matrix3 = M.Matrix([[1,2],[0,0],[2,2],[1,4]])
# matrix4 = M.Matrix([[0,1,1,5], [-1,-2,-3,0]])
# matrix5 = M.Matrix([[8,0,5,11,5], [16,13,18,9,16], [0,1,1,15,19], [2,1,12,17,10], [14,7,12,0,12]])

# print(matrix1.trace())
# print(matrix1.pow(3))
# print(matrix1.transpose())
# print(matrix1.inverse())

# print(matrix1 == matrix2 + matrix1 - matrix2)
# print(matrix1 + matrix2)
# print(matrix1 - matrix2)
# print(matrix3 * matrix4)

# npmatrix1 = np.array([[1,2,-1], [2,1,2], [-1,2,1]])
# npmatrix2 = np.array([[8,0,5,11,5], [16,13,18,9,16], [0,1,1,15,19], [2,1,12,17,10], [14,7,12,0,12]])


# Generate matrices of a given dimension (n) that are invertable 
def randomMatrix(n):
    return np.vander(np.arange(n), n)

timeNPInvert = []
timeNPLinalgInv = []
timeInverse = []

n = 1000

# Max dimension for np.linalg.inv is 124

for i in range(n):
    # Time for np.invert
    t1NPInvert = t.default_timer()

    np.invert(randomMatrix(i))

    t2NPInvert = t.default_timer()

    timeNPInvert.append(t2NPInvert-t1NPInvert)

    # Time for np.linalg.inv
    t1NPLinalgInv = t.default_timer()
    
    np.linalg.inv(randomMatrix(i))

    t2NPLinalgInv = t.default_timer()

    timeNPLinalgInv.append(t2NPLinalgInv-t1NPLinalgInv)

    # Time for self programmed function 
    t1Inverse = t.default_timer()
        
    M.Matrix(randomMatrix(10).tolist()).inverse()

    t2Inverse = t.default_timer()

    timeInverse.append(t2Inverse-t1Inverse)


#print(timeNPInvert)
#print(timeNPLinalgInv)  
#print(timeInverse)

dataX = np.arange(n)


plt.figure(1)

plt.title('Time for calculating the inverse of a vander matrix with dimension n')

plt.plot(dataX, timeNPInvert, 'b*', label='Numpy Invert function')
# plt.plot(dataX, timeNPLinalgInv, 'r*', label='Numpy linalg function')
plt.plot(dataX, timeInverse, 'g*', label='Python Invert function')

plt.xlabel('Dimension (n)')
plt.ylabel('Computing time')
plt.legend()

plt.show()