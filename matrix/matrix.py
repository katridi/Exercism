class Matrix(object):
    def __init__(self, matrix_string):
        self.matrix = [[int(x) for x in y.split()] for y in matrix_string.split('\n')] 
    def row(self, index):
        return self.matrix[index-1]

    def column(self, index):
        return [self.matrix[i][index-1] for i in range(len(self.matrix))]
