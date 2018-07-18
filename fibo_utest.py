import unittest

import fibo


class FiboTest_0(unittest.TestCase):
    def test_fibo_0(self):
        self.assertEqual(fibo.fibo(10, 20), None)


class FiboTest_1(unittest.TestCase):
    def test_fibo_0(self):
        self.assertEqual(fibo.fibo(1, 20), None)


class FiboTest_2(unittest.TestCase):
    def test_fibo_0(self):
        self.assertEqual(fibo.fibo(20, 10), None)


class FiboTest_3(unittest.TestCase):
    def test_fibo_0(self):
        self.assertEqual(fibo.fibo(100, 200), None)


if __name__ == '__main__':
    unittest.main()
