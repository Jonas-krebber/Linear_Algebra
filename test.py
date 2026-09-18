import Matrix as M
import numpy as np

matrix1 = M.Matrix([[1,2,-1], [2,1,2], [-1,2,1]])
matrix2 = M.Matrix([[1,1,0], [1,1,0], [1,1,1]])

matrix3 = M.Matrix([[1,2],[0,0],[2,2],[1,4]])
matrix4 = M.Matrix([[0,1,1,5], [-1,-2,-3,0]])

print(matrix1.trace())
print(matrix1.pow(3))
print(matrix1.transpose())
print(matrix1.inverse())

print(matrix1 == matrix2 + matrix1 - matrix2)
print(matrix1 + matrix2)
print(matrix1 - matrix2)
print(matrix3 * matrix4)