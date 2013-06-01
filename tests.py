from mbyn import mbyn
import unittest

A = [
        [2, 3],
        [3, 3]
    ]

B = [
        [2, 5, 6],
        [2, 3, 2]
    ]

C = [
        [0, 0, 1],
        [3, 3]
    ]

D = [
        [1.0, 0.0, 2.0, 0.0, 0.0],
        [0.0, 1.0, 0.0, 1.0, 0.0],
        [0.0, 0.0, 1.0, 0.0, 0.0],
        [0.0, 0.0, 0.0, 0.0, 1.0]
]

class MByNTests(unittest.TestCase):

    def test_add(self):
        result = mbyn.add([A, A])
        self.assertEqual(result, [[4, 6],[6, 6]])

    def test_addRows(self):
        result = mbyn.addRows(B[0], B[1])
        self.assertEquals(result, [4, 8, 8])

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
  
    def test_getColumn(self):
        result = mbyn.getColumn(B, 2)
        self.assertEqual(result, [6, 2])

    def test_getIdentityMatrix(self):
        result = mbyn.getIdentityMatrix(4)
        self.assertEqual(result, [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
    
    def test_getReducedRowEchelonForm(self):
        result = mbyn.getReducedRowEchelonForm(D)
        self.assertEquals(result, [[1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 1.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0]])

    def test_getTranspose(self):
        result = mbyn.getTranspose(B)
        self.assertEqual(result, [[2, 2], [5, 3],[6, 2]])
    
    def test_initialize(self):
        result = mbyn.initialize(3, 5, 1)
        self.assertEqual(result, [[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]])
    
    def test_isRowEchelonForm(self):
        result = mbyn.isRowEchelonForm(D)
        self.assertTrue(result)
        result = mbyn.isRowEchelonForm(B)
        self.assertFalse(result)

    def test_isSqaure(self):
        result = mbyn.isSquare(A)
        self.assertTrue(result)

        result = mbyn.isSquare(B)
        self.assertFalse(result)

    def test_multiply(self):
        result = mbyn.multiply(A, B)
        self.assertEqual(result, [[10, 19, 18], [12, 24, 24]])

    def test_multiplyRowByColumn(self):
        result = mbyn.multiplyRowByColumn([2, 3, 4], [5, 6, 7])
        self.assertEqual(result, 56)

    def test_scaleBy(self):
        result = mbyn.scaleBy(mbyn.clone(A), 4)
        self.assertEqual(result, [[8, 12], [12, 12]])

    def test_scaleRow(self):
        result = mbyn.scaleRow(A[0],  6)
        self.assertEqual(result, [12, 18])

    def test_subtractRows(self):
        a = [1, 1, 1]
        b = [2, 2, 2]
        result = mbyn.subtractRows(a, b)
        self.assertEqual(result, [-1, -1, -1])

    def test_swapRows(self):
        result = mbyn.swapRows(A, 0, 1)
        self.assertEqual(result, [[3, 3], [2, 3]])

    def test_validate(self):
        result = mbyn.validate(A)
        self.assertTrue(result)

        result = mbyn.validate([[3, 2, 1], [3, 2]])
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()
