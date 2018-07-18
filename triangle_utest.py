import unittest

import triangle


class TriangleTest(unittest.TestCase):
    def test_validation_0(self):
        self.assertEqual(triangle.validation(79), 79)

    def test_validation_1(self):
        self.assertEqual(triangle.validation(5), 5)

    def test_validation_2(self):
        self.assertEqual(triangle.validation(1), 1)

    def test_validation_3(self):
        self.assertEqual(triangle.validation(0), 0)

    def test_validation_4(self):
        self.assertEqual(triangle.validation('*'), 0)

    def test_validation_5(self):
        self.assertEqual(triangle.validation('n'), 0)

    def test_validation_6(self):
        self.assertEqual(triangle.validation(''), 0)

    def test_triangle_is_exist_0(self):
        self.assertTrue(triangle.triangle_is_exist(5, 5, 5))

    def test_triangle_is_exist_1(self):
        self.assertTrue(triangle.triangle_is_exist(5, 4, 6))

    def test_triangle_is_exist_2(self):
        self.assertTrue(triangle.triangle_is_exist(4, 3, 5))

    def test_triangle_is_exist_3(self):
        self.assertFalse(triangle.triangle_is_exist(0, 0, 0))

    def test_triangle_is_exist_4(self):
        self.assertFalse(triangle.triangle_is_exist(0, 1, 0))

    def test_triangle_is_exist_4(self):
        self.assertFalse(triangle.triangle_is_exist(1, 2, 3))

    def test_triangle_is_exist_5(self):
        self.assertFalse(triangle.triangle_is_exist(1, 100, 3))

    def test_triangle_is_valid_0(self):
        self.assertTrue(triangle.triangle_is_valid('name', 4, 3, 5))

    def test_triangle_is_valid_1(self):
        self.assertTrue(triangle.triangle_is_valid('name2', 3, 3, 3))


if __name__ == '__main__':
    unittest.main()
