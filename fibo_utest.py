import unittest

import fibo


class FiboTest(unittest.TestCase):
    def test_fibo_0(self):
        self.assertEqual(chess.validation(0), 1)

    def test_fibo_1(self):
        self.assertEqual(chess.validation(1), 1)

    def test_fibo_2(self):
        self.assertEqual(chess.validation(2), 3)

    def test_fibo_3(self):
        self.assertEqual(chess.validation(3), 6)

if __name__ == '__main__':
    unittest.main()