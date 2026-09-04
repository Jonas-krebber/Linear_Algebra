class Blockmatrix():

    def __init__(self, values, row_dim, column_dim):

        # Checks for right input - missing: Checking each nested list element
        assert isinstance(values, list), "value must be a number."
        assert len(values) == row_dim, "Issue with Matrix size"
        assert len(values[0]) == column_dim, "Issue with Matrix size"

        assert isinstance(row_dim, int), "dim must be an integer."
        assert isinstance(column_dim, int), "dim must be an integer."

        # Defining the Matrix parameters 
        self.values = values
        self.row_dim = row_dim
        self.column_dim = column_dim

    # Defining the interface for displaying the Matrix     
    def __str__(self):
        str = ''
        for i in range(self.row_dim):
            for j in range(self.column_dim):
               str += f'{self.values[i][j]} '
            str += '\n'
        return str
            

matrix1 = Blockmatrix([[2,3,3], [1,1,0]], 2, 3)

print(matrix1)

