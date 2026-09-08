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

    # Defining the interface for displaying the Matrix     
    def __str__(self):
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

        # Add the two matrices 

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
    
            # Subtract the two matrices 
    
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

        # Compares if the two matrices are equal to each other

        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                if self.matrix[i][j] != other.matrix[i][j]:
                    return False
                
        return True 

    def __mul__(self, other):

        # Checks if the computation is possible
                    
        assert len(self.matrix[0]) == len(other.matrix), "Computation not possible, check dimensions of each matrix"
                    
        # Calculate the dot product 

        newMatrix = []

        # Missing - transpose function to calculate the dot product 
        for i in range(len(self.matrix)):
            newMatrix.append([])

            for j in range(len(other.matrix[0])):
                newMatrix[i].append(0)

        return Matrix(newMatrix)

matrix1 = Matrix([[0,0,0], [0,0,0]])
matrix2 = Matrix([[0,0], [0,0], [0,0]])

print(matrix1 * matrix2)