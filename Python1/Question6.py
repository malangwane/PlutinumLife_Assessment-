import unittest

class MathOperations:
    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

class TestMath(unittest.TestCase):
    def setUp(self):
        self.math = MathOperations()

    def test_add(self):
        result = self.math.add(10, 10)
        self.assertEqual(result, 20)

    def test_subtract(self):
        result = self.math.subtract(10, 10)
        self.assertEqual(result, 0)

    def test_multiply(self):
        result = self.math.multiply(10, 10)
        self.assertEqual(result, 100)
