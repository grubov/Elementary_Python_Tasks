import unittest

import envelope


class EnvelopeTest(unittest.TestCase):
    def test_compare_is_valid_0(self):
        self.assertTrue(chess.board_is_valid(4, 4, 3, 3))

    def test_compare_is_valid_1(self):
        self.assertTrue(chess.board_is_valid(5, 10, 4, 9))

    def test_compare_is_valid_2(self):
        self.assertTrue(chess.board_is_valid(10, 5, 9, 4))

    def test_compare_is_valid_3(self):
        self.assertFalse(chess.board_is_valid(2, 2, 3, 3))

    def test_compareis_valid_4(self):
        self.assertFalse(chess.board_is_valid(1, 1, 4, 4))


if __name__ == '__main__':
    unittest.main()