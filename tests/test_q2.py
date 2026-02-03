"""Tests for Lab 1 Question 2"""

import sys
sys.path.append(".")
import unittest
from src.q2 import SpamReader


class TestSpamReader(unittest.TestCase):
    def setUp(self):
        # assumes spam.csv is in the project root (same folder you run tests from)
        self.reader = SpamReader("spam.csv")

    def test_first_five_rows_shape(self):
        first5 = self.reader.get_first_five_rows()
        self.assertEqual(len(first5), 5)

    def test_spam_only_contains_spam_labels(self):
        spam_df = self.reader.get_spam()
        # all labels in v1 should be "spam"
        self.assertTrue((spam_df["v1"] == "spam").all())

    def test_ham_only_contains_ham_labels(self):
        ham_df = self.reader.get_ham()
        # all labels in v1 should be "ham"
        self.assertTrue((ham_df["v1"] == "ham").all())

    def test_missing_file_raises_value_error(self):
        with self.assertRaises(ValueError):
            SpamReader("definitely_not_a_real_file_12345.csv")


if __name__ == "__main__":
    unittest.main()