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
    
    def test_fill(self):
        result = mbyn.fill(C, 1)
        self.assertEqual(result, [[0, 0, 1], [3, 3, 1]])

    def test_isSqaure(self):
        result = mbyn.isSquare(A)
        self.assertTrue(result)

    def test_multiply(self):
        result = mbyn.multiply(A, B)
        self.assertEqual(result, [[10, 19, 18], [12, 24, 24]])

if __name__ == '__main__':
    unittest.main()
