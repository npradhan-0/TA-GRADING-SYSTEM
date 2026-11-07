import sys
import os
import unittest

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from main import load_roster


class test_load_roster(unittest.TestCase):

    def setUp(self):
        with open("Roster.csv", "w") as f:
            f.write("Student ID,Email address\n123,s1@oswego.edu\n234,s2@oswego.edu\n")

        with open("empty.csv", "w") as f:
            f.write("")

    def tearDown(self):
        if os.path.exists("Roster.csv"):
            os.remove("Roster.csv")

        if os.path.exists("empty.csv"):
            os.remove("empty.csv")

    def test_load_roster_tc01(self):
        result = load_roster("abc.csv")
        self.assertEqual(result, {})

    def test_load_roster_tc02(self):
        result = load_roster("Roster.csv")
        self.assertEqual(result, {"123": "s1@oswego.edu", "234": "s2@oswego.edu"})

    def test_load_roster_tc03(self):
        result = load_roster("empty.csv")
        self.assertEqual(result, {})

    def test_load_roster_tc04(self):
        with self.assertRaises(Exception):
            load_roster(123)


if __name__ == '__main__':
    unittest.main()