import unittest

import sequence


class SequenceTest(unittest.TestCase):
    def test_validation_0(self):
        self.assertEqual(sequence.validation(79), 79)

    def test_validation_1(self):
        self.assertEqual(sequence.validation(5), 5)

    def test_validation_2(self):
        self.assertEqual(sequence.validation(1), 1)

    def test_validation_3(self):
        self.assertEqual(sequence.validation(0), 0)

    def test_validation_4(self):
        self.assertEqual(sequence.validation('*'), 0)


if __name__ == '__main__':
    unittest.main()
