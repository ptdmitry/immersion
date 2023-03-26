import unittest
from task_14_matrix import Matrix


class MatrixOperations(unittest.TestCase):
    m1 = Matrix(([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
    m2 = Matrix(([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))

    def test_add_matrix(self):
        self.assertEqual(self.m1 + self.m2, Matrix(([[2, 4, 6], [8, 10, 12], [14, 16, 18]])))

    def test_equal_matrix(self):
        self.assertEqual(self.m1 == self.m2, True)

    def test_not_equal_matrix(self):
        self.assertEqual(self.m1 != self.m2, False)

    def test_greater_matrix(self):
        self.assertEqual(Matrix(([[2, 4, 6], [8, 10, 12], [14, 16, 18]])) > self.m2, True)

    def test_less_matrix(self):
        self.assertEqual(Matrix(([[2, 4, 6], [8, 10, 12], [14, 16, 18]])) < self.m1, False)


if __name__ == '__main__':
    unittest.main(verbosity=2)
