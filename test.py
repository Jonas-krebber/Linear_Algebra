import Matrix as M
import numpy as np
import timeit as t

matrix1 = M.Matrix([[1,2,-1], [2,1,2], [-1,2,1]])
matrix2 = M.Matrix([[1,1,0], [1,1,0], [1,1,1]])

matrix3 = M.Matrix([[1,2],[0,0],[2,2],[1,4]])
matrix4 = M.Matrix([[0,1,1,5], [-1,-2,-3,0]])
matrix5 = M.Matrix([[8,0,5,11,5], [16,13,18,9,16], [0,1,1,15,19], [2,1,12,17,10], [14,7,12,0,12]])

print(matrix1.trace())
print(matrix1.pow(3))
print(matrix1.transpose())
print(matrix1.inverse())

print(matrix1 == matrix2 + matrix1 - matrix2)
print(matrix1 + matrix2)
print(matrix1 - matrix2)
print(matrix3 * matrix4)

npmatrix1 = np.array([[1,2,-1], [2,1,2], [-1,2,1]])
npmatrix2 = np.array([[8,0,5,11,5], [16,13,18,9,16], [0,1,1,15,19], [2,1,12,17,10], [14,7,12,0,12]])

# Time for np.invert
npt1 = t.default_timer()

np.invert(npmatrix2)

npt2 = t.default_timer()

difnp = npt2-npt1

print(difnp, 'Time for np.invert()')

# Time for np.linal.inv()
nplint1 = t.default_timer()

np.linalg.inv(npmatrix2)

nplint2 = t.default_timer()

difnplin = nplint2-nplint1

print(difnplin, 'Time for np.linalg.inv()')


# Time for M.inverse()
t1 = t.default_timer()

matrix5.inverse()

t2 = t.default_timer()

difM = t2-t1

print(difM, 'Time for M.inverse()')

# print(difM/difnp)
# print(difnp/difM)