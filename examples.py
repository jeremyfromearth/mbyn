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

    G = [
            [0.0, 0.0, 1.0, 2.0],
            [0.0, -1.0, 7.0, 8.0],
            [0.0, 0.0, 0.0, 1.0],
            [3.0, -2.0, 1.0, 1.0]
    ]

    H = [
            [1.0, 2.0, 3.0],
            [4.0, 5.0, 6.0],
            [7.0, 8.0, 9.0],
            [10.0, 11.0, 12.0],
            [13.0, 14.0, 15.0]
    ]
    print 'A='
    print_matrix(A)

    print 'B='
    print_matrix(B)

    print 'C='
    print_matrix(C)

    print 'D='
    print_matrix(D)

    print 'E='
    print_matrix(E)

    print 'F='
    print_matrix(F)

    print 'G='
    print_matrix(G)

    print 'H='
    print_matrix(H)

    print 'add([A, B])'
    print_matrix(mbyn.add([A, B]))

    print 'add_rows(A[0], A[1])'
    print mbyn.add_rows(A[0], A[1])
    print '\n'

    print 'clone(A)'
    print_matrix(mbyn.clone(A))

    print 'direct_sum(A, B)'
    print_matrix(mbyn.direct_sum(A, B))

    print 'expo(A, 3)'
    print_matrix(mbyn.expo(A, 3))

    print 'fill([[0, 2], [2, 1, 3, 4]], 21)'
    print_matrix(mbyn.fill([[0, 2], [2, 1, 3, 4]], 9))

    print 'get_column(A, 1)'
    print mbyn.get_column(A, 1)
    print '\n'

    print 'get_identity_matrix(6)'
    print_matrix(mbyn.get_identity_matrix(6))

    print 'get_reduced_row_echelon_form(H)'
    print_matrix(mbyn.get_reduced_row_echelon_form(H))
    
    print 'get_sparse_matrix(E)'
    print_matrix(mbyn.get_sparse_matrix(E))

    print 'get_transpose(A)'
    print_matrix(mbyn.get_transpose(A))
    
    print 'initialize(5, 3, 0)'
    print_matrix(mbyn.initialize(5, 3, 0))

    print 'is_row_echelon_form(E)'
    print mbyn.is_row_echelon_form(E)
    print '\n'

    print 'is_square(A)'
    print mbyn.is_square(A)
    print '\n'

    print 'multpily(A, B)'
    print_matrix(mbyn.multiply(A, B))

    print 'multiply_row_by_column([3, 2, 1], [1, 4, 3])'
    print mbyn.multiply_row_by_column([3, 2, 1], [1, 4, 3])
    print '\n'
    
    print 'scale_by(A, -3)'
    print_matrix(mbyn.scale_by(A, -3))

    print 'swap_rows(A, 2, 0)'
    print_matrix(mbyn.swap_rows(A, 2, 0))

    print 'validate([[2, 1, 4], [2, 1]])'
    print mbyn.validate([[2, 1, 4],[2, 1]])

def print_matrix(matrix):
    print mbyn.to_str(matrix) + '\n'

if __name__ == '__main__':
    main()
