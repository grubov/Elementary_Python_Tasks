import unittest

import envelope


class EnvelopeTest(unittest.TestCase):
    def test_compare_0(self):
        self.assertTrue(envelope.compare(4, 5, 3, 2))

    def test_compare_1(self):
        self.assertTrue(envelope.compare(10, 5, 4, 9))

    def test_compare_2(self):
        self.assertTrue(envelope.compare(5, 5, 4, 4))

    def test_compare_3(self):
        self.assertFalse(envelope.compare(4, 4, 5, 5))

    def test_compare_4(self):
        self.assertFalse(envelope.compare(4, 9, 10, 5))


if __name__ == '__main__':
    unittest.main()
