from mbyn import mbyn
import unittest


class MbyNTests(unittest.TestCase):

    def setUp(self):
        self.A = [
                    [2, 3],
                    [3, 3]
                ]

        self.B = [
                    [2, 5, 6],
                    [2, 3, 2],
                ]

        self.C = [
                    [0, 0, 1],
                    [3, 3]
                ]
   
    def test_isSqaure(self):
        result = mbyn.isSquare(self.A)
        self.assertTrue(result)

    def test_multiply(self):
        result = mbyn.multiply(self.A, self.B)
        self.assertEqual(result, [[10, 19, 18], [12, 24, 24]])

    def test_fill(self):
        result = mbyn.fill(self.C, 1)
        self.assertEqual(result, [[0, 0, 1], [3, 3, 1]])

if __name__ == '__main__':
    unittest.main()
