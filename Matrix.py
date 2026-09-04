class Blockmatrix():

    def __init__(self, values):

        # Checks for right input - missing: Checking each nested list element
        assert isinstance(values, list), "value must be a number."

        # Defining the Matrix parameters 
        self.values = values

    # Defining the interface for displaying the Matrix     
    def __str__(self):
        str = ''
        for i in range(len(self.values)):
            for j in range(len(self.values[0])):
               str += f'{self.values[i][j]} '
            str += '\n'
        return str
            

matrix1 = Blockmatrix([[2,3,3], [1,1,0]])

print(matrix1)

