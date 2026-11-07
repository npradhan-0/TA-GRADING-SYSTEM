import sys
import os
import unittest
import tempfile

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from main import create_index_html


class test_create_index_html(unittest.TestCase):

    def setUp(self):
        self.test_dir = tempfile.TemporaryDirectory()
        self.original_dir = os.getcwd()
        os.chdir(self.test_dir.name)

        os.makedirs("reports", exist_ok=True)

    def tearDown(self):
        os.chdir(self.original_dir)
        self.test_dir.cleanup()

    def test_create_index_html_tc01(self):
        roster = {"123": "a@example.com", "234": "b@example.com"}
        create_index_html(roster)
        self.assertEqual(os.path.exists("index.html"), True)

    def test_create_index_html_tc02(self):
        create_index_html({})
        self.assertEqual(os.path.exists("index.html"), True)

    def test_create_index_html_tc03(self):
        with self.assertRaises(Exception):
            create_index_html("123")

    def test_create_index_html_tc04(self):
        with self.assertRaises(Exception):
            create_index_html(None)

    def test_create_index_html_tc05(self):
        roster = {"123": "a@example.com"}
        create_index_html(roster)
        self.assertEqual(os.path.exists("index.html"), True)


if __name__ == '__main__':
    unittest.main()