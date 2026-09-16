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
        M = []

        for i in range(len(self.matrix)):
            M.append([])

            for j in range(len(self.matrix[0])):
                M[i].append(self.matrix[i][j] + other.matrix[i][j])

        return Matrix(M)

    def __sub__(self, other):
    
            # Checks if the computation is possible
            assert len(self.matrix) == len(other.matrix), "Computation not possible, check row dimension"
            assert len(self.matrix[0]) == len(other.matrix[0]), "Computation not possible, check column dimension"
    
            # Subtract the two matrices for A - B
            M = []
    
            for i in range(len(self.matrix)):
                M.append([])

                for j in range(len(self.matrix[0])):
                    M[i].append(self.matrix[i][j] - other.matrix[i][j])
    
            return Matrix(M)

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
        M = [[self.matrix[j][i] for j in range(len(self.matrix))] for i in range(len(self.matrix[0]))]

        return Matrix(M)

    def __mul__(self, other):

        # Checks if the computation is possible          
        assert len(self.matrix[0]) == len(other.matrix), "Computation not possible, check dimensions of each matrix"
                    
        # Calculate the dot product for A * B
        M = []

        other = other.transpose()

        for i in range(len(other.matrix)):
            M.append([])

            for j in range(len(self.matrix)):

                total = sum([self.matrix[j][k] * other.matrix[i][k] for k in range(len(self.matrix[0]))])

                M[i].append(total)
                
        return Matrix(M).transpose()

    def pow(self, power):

        # Check if the Matrix is square
        assert len(self.matrix) == len(self.matrix[0]), "Matrix is not square"

        # Calculate the power of the matrix as in A^3
        M = self

        for i in range(1, power):
            M = M * self

        return M

    def trace(self):

        # Check if the Matrix is square
        assert len(self.matrix) == len(self.matrix[0]), "Matrix is not square"

        total = sum([self.matrix[i][i] for i in range(len(self.matrix))])

        return total

    def inverse(self):

        # Check if the Matrix is square
        assert len(self.matrix) == len(self.matrix[0]), "Matrix is not square"

        # define the dimension of the matrix
        dim = len(self.matrix)

        # Create Identitiy matrix
        I = [[1 if i == j else 0 for j in range(len(self.matrix))] for i in range(len(self.matrix[0]))]

        # Create a copy of the original matrix 
        M = self.matrix.copy()

        # Starting the Gauss-Jordan algorithm from the top right corner: loop through each column skipping the first 
        for h in range(1, dim):
            # Loop through each row of the matrix 
            for i in range(dim-1):
            
                # Checks (for each row) if the last -ith element of the ith row is zero (saving computation time - missing
                # Checks if the current row is smaller than the previous one (h)
                if i < dim -h:

                    # Calculate new row: Take each element of the current row and subtract the corresponding element of the last -ith row multiplied by a factor based on the current value => Should yield 0
                    newRowM = [M[i][j] - M[i][dim-h]/M[dim-h][dim-h]*M[dim-h][j] for j in range(dim)]

                    #Repeat the operation on the identity matrix 
                    newRowI = [I[i][j] - M[i][dim-h]/M[dim-h][dim-h]*I[dim-h][j] for j in range(dim)]

                    # Append the new rows to the new matrix and the identity matrix 
                    M[i] = newRowM
                    I[i] = newRowI           
                else:
                    pass

        # Continue Gauss-Jordan Algorithm for the bottom left corner: loop through each column except for the last 
        for h in range(dim-1):
            # Loop through each row of the matrix (backwards)
            for i in range(dim-1,-1,-1):
                
                # Checks if the current row is larger than the previous one (h)
                if i > h:
                    
                    # Calculate new row: Take each element of the current row and subtract the corresponding element of the last -ith row multiplied by a factor based on the current value => Should yield 0
                    newRowM = [M[i][j] - M[i][h]/M[h][h]*M[h][j] for j in range(dim)]

                    #Repeat the operation on the identity matrix 
                    newRowI = [I[i][j] - M[i][h]/M[h][h]*I[h][j] for j in range(dim)]

                    # Append the new rows to the new matrix and the identity matrix 
                    M[i] = newRowM
                    I[i] = newRowI       
                else:
                    pass

        # Turn all missing values of the original matrix to 1

        

        # implement a sorting algorithm to align the matrix with the correct shape 
        # turn all values to 1 
        # debug for no solution 

        return I, M
        
matrix1 = Matrix([[1,2,-1], [2,1,2], [-1,2,1]])
matrix2 = Matrix([[2,0,3], [1,1,0], [1,1,1]])

#print(matrix1.transpose())
#print(matrix1.pow(3) * matrix2)

#print(matrix1.trace())

print('final:',matrix1.inverse())

#print( matrix1 * matrix2)