import unittest
from fibbonacci import calcFib


class TestCase(unittest.TestCase):

    def test_fib(self):
        self.assertEqual(calcFib(2),1)
    def test_fib1(self):
        self.assertEqual(calcFib(5), 3)
    def test_fib2(self):
        self.assertEqual(calcFib(0), 0)
    def test_fib3(self):
        self.assertEqual(calcFib(-1), None)

if __name__ == '__main__':
    unittest.main(verbosity=2)