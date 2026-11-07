import sys
import os
import unittest

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from main import remove_overlapping_items


class test_remove_overlapping_items(unittest.TestCase):
    def test_remove_overlapping_items_tc01(self):
        text = "Abcd 123 npradhan@os.edu"
        patterns = [r'\d+', r'\b\w+\b']
        result = remove_overlapping_items(text, patterns)
        self.assertEqual(result, "  ")

    def test_remove_overlapping_items_tc02(self):
        text = ""
        patterns = [r'\d+', r'\b\w+\b']
        result = remove_overlapping_items(text, patterns)
        self.assertEqual(result, "")

    def test_remove_overlapping_items_tc03(self):
        with self.assertRaises(Exception):
            remove_overlapping_items(["1", 0], [r'\d+', r'\b\w+\b'])

    def test_remove_overlapping_items_tc04(self):
        text = "Abcd 123 npradhan@os.edu"
        patterns = []
        result = remove_overlapping_items(text, patterns)
        self.assertEqual(result, "Abcd 123 npradhan@os.edu")

    def test_remove_overlapping_items_tc05(self):
        text = "Abcd 123 npradhan@os.edu"
        with self.assertRaises(Exception):
            remove_overlapping_items(text, [r'[\d+'])

    def test_remove_overlapping_items_tc06(self):
        text = "Abcd 123 npradhan@os.edu"
        with self.assertRaises(Exception):
            remove_overlapping_items(text, "a")

    def test_remove_overlapping_items_tc07(self):
        text = "Abcdggh"
        patterns = [r'\d+']
        result = remove_overlapping_items(text, patterns)
        self.assertEqual(result, "Abcdggh")

    def test_remove_overlapping_items_tc08(self):
        text = "123 12"
        patterns = [r'\d+']
        result = remove_overlapping_items(text, patterns)
        self.assertEqual(result, "  ")


if __name__ == '__main__':
    unittest.main()