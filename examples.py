from mbyn import mbyn 

A = (
        (0, 1, 3),
        (1, 2, 3),
        (5, 4, 3)
)

B = (
        (0, 1, 3),
        (3, 5, 6),
        (1, 3, 9)
)

C = (
        (2, 8, 5),
        (1, 2, 3),
        (1, 1, 0)
)

D = (
        [1, 4, 32],
        [0, 0],
        [34, 34, 12, 34]
)

E = [
        [1, 2, -1],
        [0, 3, 7]
]

#print mbyn.add([A, B])
#print mbyn.initialize(4, 5, 1)
print mbyn.scaleBy(E, .5)
