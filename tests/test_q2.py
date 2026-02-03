"""Tests for Lab 1 Question 2"""

import sys
sys.path.append(".")
import unittest
from src.q2 import SpamReader
import pandas as pd


class TestSpamReader(unittest.TestCase):
    def setUp(self):
        self.reader = SpamReader("spam.csv")

    def test_first_five_rows_count(self):
        first_five = self.reader.get_first_five_rows()
        self.assertEqual(len(first_five), 5)

    def test_spam_labels(self):
        spam_df = self.reader.get_spam()
        self.assertTrue((spam_df["v1"] == "spam").all())

    def test_ham_labels(self):
        ham_df = self.reader.get_ham()
        self.assertTrue((ham_df["v1"] == "ham").all())

    def test_missing_file_raises_value_error(self):
        with self.assertRaises(ValueError):
            SpamReader("this_file_does_not_exist.csv")


if __name__ == "__main__":
    unittest.main()