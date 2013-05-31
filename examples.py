"""
Examples
"""

print "M by N Examples: \n"

from mbyn import mbyn

def main():
    A = [
            [8, 3, 4],
            [21, 3, 7],
            [3, 5, 2]
    ]

    B = [
            [5, 3, 1], 
            [1, 9, 4],
            [3, 6, 1]
    ]

    C = [
            [1, 2],
            [3, 6],
            [3, 1]
    ]

    D = [
            [1, 0, 0],
            [0, 3, 1],
            [0, 0, 4]
    ]

    E = [
            [1, 0, 2, 0, 0],
            [0, 1, 0, 1, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 0, 0, 1]
    ] 
    
    F = [
        [1, 0],
        [0, 1]
    ]

    print 'A='
    printMatrix(A)

    print 'B='
    printMatrix(B)

    print 'C='
    printMatrix(C)

    print 'D='
    printMatrix(D)

    print 'E='
    printMatrix(E)

    print 'F='
    printMatrix(F)

    print 'add([A, B])'
    printMatrix(mbyn.add([A, B]))

    print 'addRows(A[0], A[1])'
    print mbyn.addRows(A[0], A[1])
    print '\n'

    print 'clone(A)'
    printMatrix(mbyn.clone(A))

    print 'directSum(A, B)'
    printMatrix(mbyn.directSum(A, B))

    print 'expo(A, 3)'
    printMatrix(mbyn.expo(A, 3))

    print 'fill([[0, 2], [2, 1, 3, 4]], 21)'
    printMatrix(mbyn.fill([[0, 2], [2, 1, 3, 4]], 9))

    print 'getColumn(A, 1)'
    print mbyn.getColumn(A, 1)
    print '\n'

    print 'getIdentityMatrix(6)'
    printMatrix(mbyn.getIdentityMatrix(6))
    
    print 'getTranspose(A)'
    printMatrix(mbyn.getTranspose(A))
    
    print 'initialize(5, 3, 0)'
    printMatrix(mbyn.initialize(5, 3, 0))

    print 'isRowEchelonForm(E)'
    print mbyn.isRowEchelonForm(E)
    print '\n'

    print 'isSquare(A)'
    print mbyn.isSquare(A)
    print '\n'

    print 'multpily(A, B)'
    printMatrix(mbyn.multiply(A, B))

    print 'multiplyRowByColumn([3, 2, 1], [1, 4, 3])'
    print mbyn.multiplyRowByColumn([3, 2, 1], [1, 4, 3])
    print '\n'
    
    print 'rowEchelonForm(D)'
    printMatrix(mbyn.rowEchelonForm(D))

    print 'scaleBy(A, -3)'
    printMatrix(mbyn.scaleBy(A, -3))

    print 'swapRows(A, 2, 0)'
    printMatrix(mbyn.swapRows(A, 2, 0))

    print 'validate([[2, 1, 4], [2, 1]])'
    print mbyn.validate([[2, 1, 4],[2, 1]])

def printMatrix(matrix):
    print mbyn.toString(matrix) + '\n'

if __name__ == '__main__':
    main()
