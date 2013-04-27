from mbyn import mbyn
import unittest

A = [
        [2, 3],
        [3, 3]
    ]

B = [
        [2, 5, 6],
        [2, 3, 2],
    ]

C = [
        [0, 0, 1],
        [3, 3]
    ]

class MbyNTests(unittest.TestCase):

    def test_add(self):
        result = mbyn.add([A, A])
        self.assertEqual(result, [[4, 6],[6, 6]])

    def test_clone(self):
        result = mbyn.clone(B)
        self.assertEquals(result, B)

    def test_directSum(self):
        result = mbyn.directSum(A, B)
        self.assertEquals(result, [[2, 3, 0, 0, 0],[3, 3, 0, 0, 0],[0, 0, 2, 5, 6],[0, 0, 2, 3, 2]])
    
    def test_expo(self):
        result = mbyn.expo(A, 3)
        self.assertEquals(result, [[71, 84],[84, 99]])

    def test_fill(self):
        result = mbyn.fill(C, 1)
        self.assertEqual(result, [[0, 0, 1], [3, 3, 1]])

    def test_getIdentityMatrix(self):
        result = mbyn.getIdentityMatrix(4)
        self.assertEqual(result, [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])

    def test_isSqaure(self):
        result = mbyn.isSquare(A)
        self.assertTrue(result)

    def test_multiply(self):
        result = mbyn.multiply(A, B)
        self.assertEqual(result, [[10, 19, 18], [12, 24, 24]])

if __name__ == '__main__':
    unittest.main()
