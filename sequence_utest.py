import unittest

import chess


class ChessTest(unittest.TestCase):
    def test_validation_0(self):
        self.assertEqual(chess.validation(79), 79)

    def test_validation_1(self):
        self.assertEqual(chess.validation(5), 5)

    def test_validation_2(self):
        self.assertEqual(chess.validation(1), 1)

    def test_validation_3(self):
        self.assertEqual(chess.validation(0), 0)

    def test_validation_4(self):
        self.assertEqual(chess.validation('*'), 0)

    def test_validation_5(self):
        self.assertEqual(chess.validation('n'), 0)

    def test_validation_6(self):
        self.assertEqual(chess.validation(''), 0)

    def test_board_is_valid_0(self):
        self.assertTrue(chess.board_is_valid(1, 1))

    def test_board_is_valid_1(self):
        self.assertTrue(chess.board_is_valid(1, 2))

    def test_board_is_valid_2(self):
        self.assertTrue(chess.board_is_valid(79, 79))

    def test_board_is_valid_3(self):
        self.assertFalse(chess.board_is_valid(0, 0))

    def test_board_is_valid_4(self):
        self.assertFalse(chess.board_is_valid(0, 1))


if __name__ == '__main__':
    unittest.main()