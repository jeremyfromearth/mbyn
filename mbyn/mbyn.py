"""
m-by-n
A module for linear algebra matrix operations
Matrix arguments should be formatted as such:
    Row matrix (list): 
        [x, y, z]
    Row matrix (tuple): 
        (x, y, z) 
    Column matrix (list): 
        [x1, x2, x3]
    2x3 matrix (list): 
        [[a, b, c], [x, y, z]]
    4x4 matrix (tuple): 
        ((a, b, c, d), (e, f, g, h), (i, j, k, l), (m, n, o, p))
    
Generally, error handling is pretty light. Matrices are expected to be compatible 
however appropriate to the operation they are being supplied to. There are a number
of validation methods that should aid in testing for compatability in cases where
formatting integrity is unknown. 
"""

def add(matrices):
    """
    Adds multiple matrices
    Only matrices of identical dimension can be added
    The dimension of the first matrix in the list is used to initialize the result matrix
    If any of the subsequent matrices are not of the same dimension as the initialized, range errors are thrown
    """
    if len(matrices) is 0:
        return None

    if len(matrices) is 1:
        return matrices[0]

    result = initialize(len(matrices[0]), len(matrices[0][0]))
    
    for row in xrange(0, len(result)): 
        for matrix in matrices:
            for col in xrange(0, len(result[row])):
                result[row][col] += matrix[row][col]
                pass
    return result


def addRows(matrix, a, b):
    """
    Add two rows of a matrix
    Row a will be added to row b
    """
    pass


def clone(matrix):
    """
    Clones a matrix
    """
    result = []
    for i in xrange(0, len(matrix)):
        result.append([])
        for j in xrange(0, len(matrix[i])):
            result[i].append(matrix[i][j])
    return result


def directSum(a, b):
    """
    Returns the direct sum of the two supplied matrices
    """
    rows = len(a) + len(b)
    cols = len(a[0]) + len(b[0])
    result = initialize(rows, cols)
    for i in xrange(0, len(a)):
        for j in xrange(0, len(a[i])):
            result[i][j] = a[i][j]

    for i in xrange(0, len(b)):
        for j in xrange(0, len(b[i])):
            result[len(a) + i][len(a[0]) + j] = b[i][j]
    return result


def expo(matrix, exponent):
    """
    Raise a matrix to a power
    """
    if not isSquare(matrix): return None
    result = clone(matrix) 
    for x in range(0, exponent - 1):
        result = multiply(matrix, result)
    return result


def fill(matrix, value=0):
    """
    Fills in a missing columns of a matrix with supplied "value" param
    Rows of the supplied matrix must be lists (mutable) as this function will add indices to short rows
    """
    max = 0
    for row in xrange(0, len(matrix)):
        columns = len(matrix[row])
        if columns > max:
            max = columns

    for row in xrange(0, len(matrix)):
        if len(matrix[row]) < max:
            while len(matrix[row]) < max:
                matrix[row].append(value)
    return matrix


def getColumn(matrix, n):
    """
    Returns a single columns of a matrix as a list (a column vector)
    """
    result = []
    for i in xrange(0, len(matrix)):
        result.append(matrix[i][n])
    return result


def getIdentityMatrix(n):
    """
    Creates an identity an matrix of dimension n
    """
    result = []
    i = 0
    while i < n:
        j = 0
        result.append([])
        while len(result[i]) < n:
            if i == j:
                result[i].append(1)
            else:
                result[i].append(0)
            j += 1
        i += 1
    return result


def getInverse(matrix):
    """
    Returns the inverse of a supplied matrix
    The inverse of matrix A is the matrix B such that A*B = the identity matrix
    """
    print 'getInverse() not implemented'
    pass


def getTranspose(matrix):
    """
    Returns the transpose of the supplied matrix
    The transpose of a matrix essentially reverses the row and columns of a matrix such that A[i][j] = B[j][i]
    """
    result = []
    num_rows = len(matrix[0])
    num_cols = len(matrix)
    
    for i in xrange(0, num_rows):
        result.append([])
        for j in xrange(0, num_cols):
            result[i].append(matrix[j][i]) 
    return result


def initialize(rows, columns, value=0):
    """
    Creates a new matrix
    """
    result = []
    for r in xrange(0, rows):
        result.append([])
        for c in xrange(0, columns):
            result[r].append(value)
    return result


def isSquare(matrix):
    """
    Returns a boolean indicating that the matrix is an n by n matrix
    It does so only by verifying that length of the entire matrix is equal to the length of the first row
    """
    return len(matrix) is len(matrix[0])


def multiply(a, b):
    """
    Multiplies two matrices 
    If a is m x n, b should be n x p, otherwise None is returned
    This method is split into a couple of steps
        * Check for multiplicative compatibility
        * Make a list of the columns of matrix b
        * Multiply the rows of matrix a by the list of columns
    """
    if len(a[0]) is not len(b):
        return None

    columns = []
    for i in xrange(0, len(b[0])):
        columns.append(getColumn(b, i))

    result = []
    for i in xrange(0, len(a)):
        result.append([])
        for j in xrange(0, len(columns)):
            result[i].append(multiplyRowByColumn(a[i], columns[j]))
    return result 


def multiplyRowByColumn(row, column):
    """
    Multplies a row by a columns and returns a single value as the result
    Will return None if the row and column are not the same length
    """
    if len(row) is not len(column):
        return None
    
    result = 0
    for i in xrange(0, len(row)):
        result += row[i] * column[i]
    return result


def partition(matrix, rows, cols):
    """
    Partitions a matrix
    """
    print 'partition not implemented'


def toString(matrix):
    """
    Returns a well formatted string representation of a matrix
    """
    result = ''
    num_rows = len(matrix)
    for i in xrange(0, num_rows):
        num_cols = len(matrix[i])
        for j in xrange(0, num_cols):
            result += str(matrix[i][j])
            if j < num_cols - 1:
                result += ', '
        
        if i < num_rows - 1:
            result += '\n'
    return result


def scaleBy(matrix, scalar):
    """
    Multiplies every value in the matrix by the supplied scalar
    """
    result = clone(matrix) 
    num_rows = len(result)
    for i in xrange(0, num_rows):
        num_cols = len(result[i])
        for j in xrange(0, num_cols):
            result[i][j] *= scalar
    return result 


def scaleRow(row, scalar):
    """
    Multiplies each value in a row by the supplied scalar
    This method directly affects the supplied matrix
    """
    result = []
    for i in xrange(0, len(row)):
       result.append(row[i] * scalar)
    return result 


def submatrix(matrix, r1, r2, c1, c2):
    """
    Returns a sub matrix of the supplied matrix
    """
    print 'submatrix not implemented'


def subtractRows(matrix, a, b):
    """
    Subtract rows of a matrix
    Row a is subtracted to row b
    """
    pass


def swapRows(matrix, a, b):
    """
    Swaps the rows of a matrix
    a & b should be the indices of the rows to swap
    """
    rowA = matrix[a]
    rowB = matrix[b]
    matrix[a] = rowB
    matrix[b] = rowA
    return matrix
    

def validate(matrix):
    """
    Returns a boolean indicating that the matrix is valid
    A valid matrix is one in which an equal number of columns is defined for each row
    """
    if len(matrix) is 0:
        return False

    if len(matrix) is 1:
        return True

    l = len(matrix[0])
    for row in matrix:
        if len(row) is not l:
            return False
    return True
