def saddle_points(matrix):
    saddle_points = []
    check_matrix(matrix)
    for en, row in enumerate(matrix):
        row_max = row.index(max(row))
        if matrix[en][row_max] <= min([matrix[i][row_max] for i in range(len(matrix))]):
            saddle_points.append((en + 1, row_max + 1))
    return set(saddle_points)
    
def check_matrix(matrix):
    first_row = len(matrix[0])
    for row in matrix:
     if len(row) != first_row:
        raise ValueError('Matrix turns out to be irregular')