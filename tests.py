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

    def test_add_rows(self):
        result = mbyn.add_rows(B[0], B[1])
        self.assertEquals(result, [4, 8, 8])

    def test_clone(self):
        result = mbyn.clone(B)
        self.assertEquals(result, B)

    def test_direct_sum(self):
        result = mbyn.direct_sum(A, B)
        self.assertEquals(result, [[2, 3, 0, 0, 0],[3, 3, 0, 0, 0],[0, 0, 2, 5, 6],[0, 0, 2, 3, 2]])
    
    def test_expo(self):
        result = mbyn.expo(A, 3)
        self.assertEquals(result, [[71, 84],[84, 99]])

    def test_fill(self):
        result = mbyn.fill(C, 1)
        self.assertEqual(result, [[0, 0, 1], [3, 3, 1]])
  
    def test_get_column(self):
        result = mbyn.get_column(B, 2)
        self.assertEqual(result, [6, 2])

    def test_get_identity_matrix(self):
        result = mbyn.get_identity_matrix(4)
        self.assertEqual(result, [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
    
    def test_get_reduced_row_echelon_form(self):
        result = mbyn.get_reduced_row_echelon_form(D)
        self.assertEquals(result, [[1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 1.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0]])

        result = mbyn.get_reduced_row_echelon_form([[0, 0, 0]])
        self.assertEquals(result, [[0, 0, 0]]);
        
        result = mbyn.get_reduced_row_echelon_form([[0, 0, 0], [1, 0, 0], [0, 1, 0]])
        self.assertEquals(result, [[1, 0, 0], [0, 1, 0], [0, 0, 0]]);

    def test_get_sparse_matrix(self):
        result = mbyn.get_sparse_matrix(D)
        self.assertEquals(result, [[0, 0, 1], [0, 2, 2], [1, 1, 1], [1, 3, 1], [2, 2, 1], [3, 4, 1]])

    def test_get_transpose(self):
        result = mbyn.get_transpose(B)
        self.assertEqual(result, [[2, 2], [5, 3],[6, 2]])
    
    def test_initialize(self):
        result = mbyn.initialize(3, 5, 1)
        self.assertEqual(result, [[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]])
    
    def test_is_row_echelon_form(self):
        result = mbyn.is_row_echelon_form(D)
        self.assertTrue(result)
        result = mbyn.is_row_echelon_form(B)
        self.assertFalse(result)

    def test_is_square(self):
        result = mbyn.is_square(A)
        self.assertTrue(result)
        result = mbyn.is_square(B)
        self.assertFalse(result)

    def test_is_zero_vector(self):
        v = [0, 0, 0, 0, 0, 0]
        self.assertTrue(mbyn.is_zero_vector(v))
        v.append(1)
        self.assertFalse(mbyn.is_zero_vector(v))

    def test_multiply(self):
        result = mbyn.multiply(A, B)
        self.assertEqual(result, [[10, 19, 18], [12, 24, 24]])

    def test_multiply_row_by_column(self):
        result = mbyn.multiply_row_by_column([2, 3, 4], [5, 6, 7])
        self.assertEqual(result, 56)

    def test_scale_by(self):
        result = mbyn.scale_by(mbyn.clone(A), 4)
        self.assertEqual(result, [[8, 12], [12, 12]])

    def test_scale_row(self):
        result = mbyn.scale_row(A[0],  6)
        self.assertEqual(result, [12, 18])

    def test_subtract_rows(self):
        a = [1, 1, 1]
        b = [2, 2, 2]
        result = mbyn.subtract_rows(a, b)
        self.assertEqual(result, [-1, -1, -1])

    def test_swap_rows(self):
        result = mbyn.swap_rows(A, 0, 1)
        self.assertEqual(result, [[3, 3], [2, 3]])

    def test_validate(self):
        result = mbyn.validate(A)
        self.assertTrue(result)

        result = mbyn.validate([[3, 2, 1], [3, 2]])
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()
