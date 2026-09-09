# Create a class called Matrix. It performs all basic functions of linear algebra in combination with any matrix.
# Current operations: +, -, *, =
# Current functions: transpose, pow

class Matrix():

    def __init__(self, matrix):

        # Checks for right input
        assert isinstance(matrix, list), "Entry must be an array"

        for i in range(len(matrix)):
            assert len(matrix[i]) == len(matrix[0]), "Matrix misses values"

            for j in range(len(matrix[i])):
                assert type(matrix[i][j]) in [int, float], "Entry must consist of only numbers"

        # Defining the Matrix parameters 
        self.matrix = matrix

    def __str__(self):

        # Defining the interface for displaying the matrix 
        str = ''

        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
               str += f'{self.matrix[i][j]} '

            str += '\n'

        return str

    def __add__(self, other):

        # Checks if the computation is possible
        assert len(self.matrix) == len(other.matrix), "Computation not possible, check row dimension"
        assert len(self.matrix[0]) == len(other.matrix[0]), "Computation not possible, check column dimension"

        # Add the two matrices for A + B
        newMatrix = []

        for i in range(len(self.matrix)):
            newMatrix.append([])

            for j in range(len(self.matrix[0])):
                newMatrix[i].append(self.matrix[i][j] + other.matrix[i][j])

        return Matrix(newMatrix)

    def __sub__(self, other):
    
            # Checks if the computation is possible
            assert len(self.matrix) == len(other.matrix), "Computation not possible, check row dimension"
            assert len(self.matrix[0]) == len(other.matrix[0]), "Computation not possible, check column dimension"
    
            # Subtract the two matrices for A - B
            newMatrix = []
    
            for i in range(len(self.matrix)):
                newMatrix.append([])

                for j in range(len(self.matrix[0])):
                    newMatrix[i].append(self.matrix[i][j] - other.matrix[i][j])
    
            return Matrix(newMatrix)

    def __eq__(self, other):

        # Checks if the computation is possible  
        assert len(self.matrix) == len(other.matrix), "Computation not possible, check row dimension"
            
        for i in range(len(self.matrix)):
            assert len(self.matrix[i]) == len(other.matrix[i]), "Computation not possible, check column dimension"

        # Compares if the two matrices are equal to each other for A == B
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                if self.matrix[i][j] != other.matrix[i][j]:
                    return False
                  
        return True 

    def transpose(self):

        # Transposes the Matrix as in A^T
        newMatrix = []

        for i in range(len(self.matrix[0])):
            newRow = []

            for j in range(len(self.matrix)):
                newRow.append(self.matrix[j][i])

            newMatrix.append(newRow)

        return Matrix(newMatrix)

    def __mul__(self, other):

        # Checks if the computation is possible          
        assert len(self.matrix[0]) == len(other.matrix), "Computation not possible, check dimensions of each matrix"
                    
        # Calculate the dot product for A * B
        newMatrix = []

        other = other.transpose()

        for i in range(len(other.matrix)):
            newMatrix.append([])

            for j in range(len(self.matrix)):
                sum = 0

                for k in range(len(self.matrix[0])):
                    sum += self.matrix[j][k] * other.matrix[i][k]

                newMatrix[i].append(sum)
                
        return Matrix(newMatrix).transpose()

    def pow(self, power):

        # Check if the Matrix is square
        assert len(self.matrix) == len(self.matrix[0]), "Matrix is not square"

        # Calculate the power of the matrix as in A^3
        newMatrix = self

        for i in range(1, power):
            newMatrix = newMatrix * self

        return newMatrix

    def trace(self):

        # Check if the Matrix is square
        assert len(self.matrix) == len(self.matrix[0]), "Matrix is not square"

        # Calculating the trace of the matrix
        sum = 0

        for i in range(len(self.matrix)):
            sum += self.matrix[i][i]

        return sum

        
matrix1 = Matrix([[1,2,3], [3,1,3], [0,0,0]])
matrix2 = Matrix([[2,0,3], [1,1,0], [1,1,1]])

print(matrix1)
print(matrix1.pow(3) * matrix2)

print(matrix1.trace())