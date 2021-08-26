import unittest

from exceptions import *
from matrix import Matrix

class TestMatrix(unittest.TestCase):

    def setUp(self):
        self.m1 = Matrix([[0]])
        self.m2a = Matrix([[1, 2], [3, 4]])
        self.m2b = Matrix([[6, 7], [8, 9]])
        self.m3a = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        self.m3b = Matrix([[-1, -2, -3], [9, 10, 11], [0, -2.5, 10]])

    def test_init(self):
        with self.assertRaises(EmptyMatrixException):
            Matrix([])
            Matrix([[]])
        with self.assertRaises(InconsistentRowDimensionsException):
            Matrix([[0, 1], [1]])

    def test_add(self):
        self.assertEqual(self.m2a + self.m2b, Matrix([[7, 9], [11, 13]]))
        with self.assertRaises(InvalidDimensionsException):
            self.m2a + self.m1

    def test_eq(self):
        self.assertEqual(self.m2a, Matrix([[1, 2], [3, 4]]))

    def test_getitem(self):
        self.assertEqual(self.m2a[0][0], 1)

    def test_mul(self):
        self.assertEqual(self.m2a * self.m2b, Matrix([[22, 25], [50, 57]]))
        with self.assertRaises(InvalidDimensionsException):
            self.m2a * self.m1
            self.m2a * self.m3a

    def test_repr(self):
        self.assertEqual(repr(self.m2a), "[1, 2]\n[3, 4]")

    def test_setitem(self):
        self.m2a[0][0] = 7
        self.assertEqual(self.m2a[0][0], 7)

    def test_sub(self):
        self.assertEqual(self.m2a - self.m2b, Matrix([[-5, -5], [-5, -5]]))
        with self.assertRaises(InvalidDimensionsException):
            self.m3b - self.m2b

    def test_scale(self):
        self.m3a.scale(2, 1)
        self.assertEqual(self.m3a,
                         Matrix([[1, 2, 3], [8, 10, 12], [7, 8, 9]]))
        with self.assertRaises(ZeroConstantException):
            self.m1.scale(0, 0)
        with self.assertRaises(BadIndexException):
            self.m1.scale(2, 1)

    def test_interchange(self):
        self.m2a.interchange(0, 1)
        self.assertEqual(self.m2a, Matrix([[3, 4], [1, 2]]))
        with self.assertRaises(BadIndexException):
            self.m3b.interchange(2, 3)

    def test_replace(self):
        self.m3a.replace(10, 1, 2)
        self.assertEqual(self.m3a,
                         Matrix([[1, 2, 3], [4, 5, 6], [47, 58, 69]]))
        with self.assertRaises(ZeroConstantException):
            self.m2a.replace(0, 1, 2)
        with self.assertRaises(BadIndexException):
            self.m2a.replace(5, 0, 2)

    def test_transpose(self):
        self.m2a.transpose()
        self.assertEqual(self.m2a, Matrix([[1, 3], [2, 4]]))

    def test_from_dimension(self):
        self.assertEqual(Matrix.from_dimension(3), Matrix([[0, 0, 0]]))

    def test_from_dimensions(self):
        self.assertEqual(Matrix.from_dimensions(3, 3),
                         Matrix([[0, 0, 0], [0, 0, 0], [0, 0, 0]]))


if __name__ == "__main__":
    unittest.main()
