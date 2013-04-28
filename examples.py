from mbyn import mbyn 

'''
A 3x3 matrix comprised of tuples
'''
A = (
        (0, 1, 3),
        (1, 2, 3),
        (5, 4, 3)
)

print 'isSquare()'
print 'A is a sqaure matrix: %s' % mbyn.isSquare(A)

'''
Similarly a 3x3 matrix comprised of lists
'''
B = [
        [0, 1, 3],
        [3, 5, 6],
        [1, 3, 9]
]

print 'isSqaure()'
print 'B is a square matrix: %s' % mbyn.isSquare(B)

C = (
        (2, 8, 5),
        (1, 2, 3),
        (1, 1, 0)
)

print 'add()'
print 'A + B + C =\n%s' %  mbyn.toString(mbyn.add([A, B, C]))

D = (
        [1, 4, 32],
        [0, 0],
        [34, 34, 12, 34]
)

print 'fill()'
print mbyn.toString(mbyn.fill(D, 10))

E = [
        [1, 2, -1],
        [0, 3, 7]
]

F = [
        [10, 8, 2],
        [3, 5, 10],
        [20, 1, 4]
]

print 'multiply()'
print mbyn.toString(mbyn.multiply(E, F))

G = [
        [2, 3],
        [4, 3]
]

H = [
        
        [4, 3, 45, 21],
        [0, 34, 22, 1],
        [78, 34, 1, 90],
        [90, 23, 1, 4]
]

print 'expo()'
print mbyn.expo(H, 2)

print 'scaleRow()'
print mbyn.scaleRow(H[0], 4)

print 'directSum(G, H)'
print mbyn.toString(mbyn.directSum(G, H))

print 'swapRows(H, 0, 1)'
print mbyn.toString(mbyn.swapRows(H, 0, 1))

print mbyn.multiply(G, G)
print mbyn.expo(G, 3)
