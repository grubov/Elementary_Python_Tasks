import unittest

import ticket


class TicketTest(unittest.TestCase):
    def test_moscow_0(self):
        self.assertTrue(ticket.moscow(111111))

    def test_moscow_1(self):
        self.assertTrue(ticket.moscow(101101))

    def test_moscow_2(self):
        self.assertFalse(ticket.moscow(123322))

    def test_moscow_3(self):
        self.assertFalse(ticket.moscow(211111))

    def test_piter_0(self):
        self.assertTrue(ticket.piter(111111))

    def test_piter_1(self):
        self.assertTrue(ticket.piter(122133))

    def test_piter_2(self):
        self.assertFalse(ticket.piter(123456))

    def test_piter_3(self):
        self.assertFalse(ticket.piter(112234))


if __name__ == '__main__':
    unittest.main()
