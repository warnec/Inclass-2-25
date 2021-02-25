import unittest
from fib import calcFib


class TestCase(unittest.TestCase):

    def test_fib(self):
        self.assertEqual(calcFib(2),1)
    def test_fib1(self):
        self.assertEqual(calcFib(5), 5)
    def test_fib2(self):
        self.assertEqual(calcFib(0), 0)

if __name__ == '__main__':
    unittest.main(verbosity=2)