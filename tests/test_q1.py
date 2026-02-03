"""Tests for Lab 1 Question 1"""

import sys
sys.path.append(".")
import unittest
from src.q1 import Calculator


class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(2.0, 3.0), 5.0)
        self.assertEqual(self.calc.add(-1.0, 1.0), 0.0)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(5.0, 3.0), 2.0)
        self.assertEqual(self.calc.subtract(2.0, 4.0), -2.0)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(2.0, 3.0), 6.0)
        self.assertEqual(self.calc.multiply(-1.0, 5.0), -5.0)

    def test_divide(self):
        self.assertEqual(self.calc.divide(6.0, 3.0), 2.0)
        self.assertEqual(self.calc.divide(-4.0, 2.0), -2.0)
        with self.assertRaises(ZeroDivisionError):
            self.calc.divide(5.0, 0.0)


if __name__ == "__main__":
    unittest.main()