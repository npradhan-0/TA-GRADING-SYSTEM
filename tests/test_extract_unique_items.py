import sys
import os
import unittest

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from main import extract_unique_items


class TestExtractUniqueItems(unittest.TestCase):

    def test_extract_unique_items_tc01(self):
        result = extract_unique_items("Cat dog bird", r'\b\w+\b')
        self.assertEqual(result, ['Cat', 'dog', 'bird'])

    def test_extract_unique_items_tc02(self):
        result = extract_unique_items("", r'\b\w+\b')
        self.assertEqual(result, [])

    def test_extract_unique_items_tc03(self):
        result = extract_unique_items("cat cat dog", r'\b\w+\b')
        self.assertEqual(result, ['cat', 'dog'])

    def test_extract_unique_items_tc04(self):
        result = extract_unique_items("Cat dog bird", r'\d+')
        self.assertEqual(result, [])

    def test_extract_unique_items_tc05(self):
        with self.assertRaises(Exception):
            extract_unique_items(["paper", "rock"], r'\b\w+\b')

    def test_extract_unique_items_tc06(self):
        with self.assertRaises(Exception):
            extract_unique_items("Cat dog bird", r'[\d+')

    def test_extract_unique_items_tc07(self):
        result = extract_unique_items("Abcd hhh", r'\d+')
        self.assertEqual(result, [])

    def test_extract_unique_items_tc08(self):
        result = extract_unique_items("abcd 100", r'\d+')
        self.assertEqual(result, ['100'])

    def test_extract_unique_items_tc09(self):
        result = extract_unique_items("10 20 30 40", r'\d+')
        self.assertEqual(result, ['10', '20', '30', '40'])

    def test_extract_unique_items_tc10(self):
        result = extract_unique_items("10 20 30 40 50", r'\d+')
        self.assertEqual(result, ['10', '20', '30', '40', '50'])

    def test_extract_unique_items_tc11(self):
        result = extract_unique_items("10 20 30 40 50 60", r'\d+')
        self.assertEqual(result, ['10', '20', '30', '40', '50'])


if __name__ == '__main__':
    unittest.main()