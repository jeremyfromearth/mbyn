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

The local variables in each method follow certain naming conventions. 
Variables m and n are used to denote the dimensions of a matrix
Variables i and j are used to denote the row index and column index of rows and columns that are iterated over

For example:
    m = len(matrix)
    for i in xrange(0, m):
        row = matrix[i]
        n = len(row)
        for j in xrange(0, n):
            column = row[j]

Where multiple matrices are iterated over or iterations are nested the convention m1, m2, n1, n2, i1, i2, j1, j2 ect.. is used
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
    
    m = len(result)
    for row in xrange(0, m): 
        for matrix in matrices:
            n = len(result[row])
            for col in xrange(0, n):
                result[row][col] += matrix[row][col]
                pass
    return result


def addRows(a, b):
    """
    Add two rows of a matrix
    Returns a new list
    """
    result = []
    
    n = len(a)
    for i in xrange(0, n):
        result.append(a[i] + b[i])
    return result


def clone(matrix):
    """
    Clones a matrix
    """
    result = []
    m = len(matrix)
    for i in xrange(0, m):
        result.append([])
        n = len(matrix[i])
        for j in xrange(0, n):
            result[i].append(matrix[i][j])
    return result


def directSum(a, b):
    """
    Returns the direct sum of the two supplied matrices
    """
    rows = len(a) + len(b)
    cols = len(a[0]) + len(b[0])
    result = initialize(rows, cols)
    m1 = len(a);
    for i in xrange(0, m1):
        n1 = len(a[i])
        for j in xrange(0, n1):
            result[i][j] = a[i][j]

    m2 = len(b)
    for i in xrange(0, m2):
        n2 = len(b[i])
        for j in xrange(0, n2):
            result[m1 + i][n1 + j] = b[i][j]
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
    m = len(matrix)
    for row in xrange(0, m):
        n = len(matrix[row])
        if n > max:
            max = n 

    for i in xrange(0, m):
        if len(matrix[i]) < max:
            while len(matrix[i]) < max:
                matrix[i].append(value)
    return matrix


def getColumn(matrix, n):
    """
    Returns a single columns of a matrix as a list (a column vector)
    """
    result = []
    m = len(matrix)
    for i in xrange(0, m):
        result.append(matrix[i][n])
    return result


def getIdentityMatrix(m):
    """
    Creates an identity an matrix of dimension n
    """
    i = 0
    result = []
    while i < m:
        j = 0
        result.append([])
        while len(result[i]) < m:
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
    m = len(matrix[0])
    n = len(matrix)
    
    for i in xrange(0, m):
        result.append([])
        for j in xrange(0, n):
            result[i].append(matrix[j][i]) 
    return result


def initialize(m, n, value=0):
    """
    Creates a new matrix
    """
    result = []
    for i in xrange(0, m):
        result.append([])
        for j in xrange(0, n):
            result[i].append(value)
    return result


def isSquare(matrix):
    """
    Returns a boolean indicating that the matrix is an n by n matrix
    It does so only by verifying that length of the entire matrix is equal to the length of the first row
    """
    m = len(matrix)
    for i in xrange(0, m):
        n = len(matrix[i])
        if m is not n:
            return False
    return True


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

    n = len(b[0])
    columns = []
    for i in xrange(0, n):
        columns.append(getColumn(b, i))

    m = len(a)
    n = len(columns)
    result = []
    for i in xrange(0, m):
        result.append([])
        for j in xrange(0, n):
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
    m = len(row)
    for i in xrange(0, m):
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
    m = len(matrix)
    for i in xrange(0, m):
        n = len(matrix[i])
        for j in xrange(0, n):
            result += str(matrix[i][j])
            if j < n - 1:
                result += ', '
        
        if i < m - 1:
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
    n = len(row)
    for i in xrange(0, n):
       result.append(row[i] * scalar)
    return result 


def submatrix(matrix, r1, r2, c1, c2):
    """
    Returns a sub matrix of the supplied matrix
    """
    print 'submatrix not implemented'


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

    n = len(matrix[0])
    for row in matrix:
        if len(row) is not n:
            return False
    return True
