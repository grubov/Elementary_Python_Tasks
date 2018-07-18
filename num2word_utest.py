import unittest

import num2word


class Num2wordTest(unittest.TestCase):
    def test_n2w_0(self):
        self.assertEqual(num2word.n2w(1), "один")

    def test_n2w_1(self):
        self.assertEqual(num2word.n2w(10), "десять")

    def test_n2w_2(self):
        self.assertEqual(num2word.n2w(101), "сто один")

    def test_n2w_3(self):
        self.assertEqual(num2word.n2w(1002), "одна тысяча два")




if __name__ == '__main__':
    unittest.main()
