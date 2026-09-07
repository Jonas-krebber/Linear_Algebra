class Blockmatrix():

    def __init__(self, values):

        # Checks for right input
        assert isinstance(values, list), "Entry must be an array"

        for i in range(len(values)):
            # Missing: Check if all arrays are of the same length

            for j in range(len(values[i])):
                assert type(values[i][j]) in [int, float], "Entry must consist of only numbers"

        # Defining the Matrix parameters 
        self.values = values

    # Defining the interface for displaying the Matrix     
    def __str__(self):
        str = ''
        for i in range(len(self.values)):
            for j in range(len(self.values[i])):
               str += f'{self.values[i][j]} '
            str += '\n'
        return str

    def __add__(self, other):

        # Checks if the computation is possible

        assert len(self.values) == len(other.values), "Computation not possible, check row dimension"

        for i in range(len(self.values)):
            assert len(self.values[i]) == len(other.values[i]), "Computation not possible, check column dimension"

        # Add the two matrices 

        newValues = []

        for i in range(len(self.values)):
            newValues.append([])
            for j in range(len(self.values[0])):
                newValues[i].append(self.values[i][j] + other.values[i][j])

        return Blockmatrix(newValues)
            

matrix1 = Blockmatrix([[2,3, 0], [1,1,0]])
matrix2 = Blockmatrix([[1,1,1], [0,0,0]])

print(matrix1 + matrix2)

