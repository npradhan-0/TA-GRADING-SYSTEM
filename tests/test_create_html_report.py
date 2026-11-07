import sys
import os
import unittest
import tempfile

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from main import create_html_report


class TestCreateHtmlReport(unittest.TestCase):

    def setUp(self):
        self.test_dir = tempfile.TemporaryDirectory()
        self.original_dir = os.getcwd()
        os.chdir(self.test_dir.name)

        os.makedirs("reports", exist_ok=True)

    def tearDown(self):
        os.chdir(self.original_dir)
        self.test_dir.cleanup()

    def test_create_html_report_tc01(self):
        create_html_report("123", {'emails': {'items': ['a@b.com'], 'count': 1, 'points': 4}}, 52)
        self.assertEqual(os.path.exists("reports/report_student_123.html"), True)

    def test_create_html_report_tc03(self):
        create_html_report("123", {'emails': {'items': ['a@b.com'], 'count': 1, 'points': 4}}, 52)
        self.assertEqual(os.path.exists("reports/report_student_123.html"), True)

    def test_create_html_report_tc04(self):
        with self.assertRaises(Exception):
            create_html_report("123", {'emails': {'items': [], 'count': 0, 'points': 0}}, 52)

    def test_create_html_report_tc05(self):
        with self.assertRaises(Exception):
            create_html_report("123", {}, 52)

    def test_create_html_report_tc06(self):
        create_html_report("123", {'emails': {'items': ['a@b.com'], 'count': 1, 'points': 4}}, 52)
        self.assertEqual(os.path.exists("reports/report_student_123.html"), True)

    def test_create_html_report_tc07(self):
        with self.assertRaises(Exception):
            create_html_report("123", {'emails': {'items': ['a@b.com'], 'count': 1, 'points': 4}}, "0")

    def test_create_html_report_tc08(self):
        create_html_report(" ", {'emails': {'items': ['a@b.com'], 'count': 1, 'points': 4}}, 52)
        self.assertEqual(os.path.exists("reports/report_student_ .html"), True)

    def test_create_html_report_tc09(self):
        create_html_report("123", {}, 52)
        self.assertEqual(os.path.exists("reports/report_student_123.html"), True)

    def test_create_html_report_tc10(self):
        create_html_report("123", {'emails': {'items': ['a@b.com'], 'count': 1, 'points': 4}, 'prices': {'items': [], 'count': 0, 'points': 0}}, 4)
        self.assertEqual(os.path.exists("reports/report_student_123.html"), True)

    def test_create_html_report_tc11(self):
        create_html_report("123", {'emails': {'items': [], 'count': 0, 'points': 0}, 'prices': {'items': [], 'count': 0, 'points': 0}}, 0)
        self.assertEqual(os.path.exists("reports/report_student_123.html"), True)

    def test_create_html_report_tc12(self):
        details = {
            'emails': {'items': ['a@b.com', 'c@d.com', 'e@f.com', 'g@h.com', 'i@j.com'], 'count': 5, 'points': 20},
            'prices': {'items': ['1', '2', '3', '4', '$5'], 'count': 5, 'points': 20},
            'phone_numbers': {'items': ['111-222-3333', '222-333-4444', '333-444-5555', '444-555-6666', '555-666-7777'], 'count': 5, 'points': 20},
            'decimals': {'items': ['1.1', '2.2', '3.3', '4.4', '5.5'], 'count': 5, 'points': 20},
            'integers': {'items': ['10', '20', '30', '40', '50'], 'count': 5, 'points': 20}
        }
        create_html_report("123", details, 100)
        self.assertEqual(os.path.exists("reports/report_student_123.html"), True)


if __name__ == '__main__':
    unittest.main()