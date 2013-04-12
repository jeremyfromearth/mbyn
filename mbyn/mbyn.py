'''
m-by-n
A module for linear algebra matrix operations
Matrix arguments should be formatted as such:
    Row matrix (list): [[x, y, z]]
    Row matrix (tuple): ((x, y, z),) (note the extra comma, this is required)
    2x3 matrix: [[a, b, c], [x, y, z]] 
'''

'''
Adds multiple matrices
Only matrices of identical dimension can be added
The dimension of the first matrix in the list is used to initialize the result matrix
If any of the subsequent matrices are not of the same dimension as the initialized, range errors are thrown
'''
def add(matrices):
    if len(matrices) is 0:
        return None

    if len(matrices) is 1:
        return matrices[0]

    result = initialize(len(matrices[0]), len(matrices[0][0]))

    for row in xrange(0, len(result)):
        for matrix in matrices:
            for col in xrange(0, len(result[row])):
                result[row][col] += matrix[row][col]
    return result

'''
Creates a new matrix
'''
def initialize(rows, columns, value=0):
    result = []
    for r in xrange(0, rows):
        result.append([])
        for c in xrange(0, columns):
            result[r].append(value)
    return result
