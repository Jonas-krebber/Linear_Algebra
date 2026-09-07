class Blockmatrix():

    def __init__(self, values):

        # Checks for right input
        assert isinstance(values, list), "Entry must be an array"

        for i in range(len(values)):
            assert len(values[i]) == len(values[0]), "Matrix misses values"

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

    def __sub__(self, other):
    
            # Checks if the computation is possible
    
            assert len(self.values) == len(other.values), "Computation not possible, check row dimension"
    
            for i in range(len(self.values)):
                assert len(self.values[i]) == len(other.values[i]), "Computation not possible, check column dimension"
    
            # Subtract the two matrices 
    
            newValues = []
    
            for i in range(len(self.values)):
                newValues.append([])
                for j in range(len(self.values[0])):
                    newValues[i].append(self.values[i][j] - other.values[i][j])
    
            return Blockmatrix(newValues)

    def __eq__(self, other):

        # Checks if the computation is possible
            
        assert len(self.values) == len(other.values), "Computation not possible, check row dimension"
            
        for i in range(len(self.values)):
            assert len(self.values[i]) == len(other.values[i]), "Computation not possible, check column dimension"

        # Compares if the two matrices are equal to each other

        for i in range(len(self.values)):
            for j in range(len(self.values[i])):
                if self.values[i][j] != other.values[i][j]:
                    return False
                
        return True 
            

matrix1 = Blockmatrix([[0,0,0], [0,0,0]])
matrix2 = Blockmatrix([[0,0,0], [0,0,0]])

print(matrix1 == matrix2)