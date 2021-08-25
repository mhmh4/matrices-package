import unittest

from matrices import Matrix


class TestMatric(unittest.TestCase):

    def setUp(self):
        m0 = Matrix()
        m1 = Matrix([[0]])
        m2a = Matrix([[1, 2], [3, 4]])
        m2b = Matrix([[6, 7], [8, 9]])
        m3a = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        m3b = Matrix([[-1, -2, -3], [9, 10, 11], [0, -2.5, 10]])

    def test_add(self):
        self.assertEqual(self.m2a + self.m2b, Matrix([[7, 9], [11, 14]]))
        with self.assertRaises(...):
            ...


if __name__ == "__main__":
    unittest.main()
