
import sys
import os
import unittest
import tempfile
import shutil

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from main import process_submissions_and_generate_reports


class test_process_submissions_and_generate_reports(unittest.TestCase):

    def setUp(self):
        self.test_dir = tempfile.TemporaryDirectory()
        self.original_dir = os.getcwd()
        os.chdir(self.test_dir.name)

        os.makedirs("submissions", exist_ok=True)
        os.makedirs("reports", exist_ok=True)

    def tearDown(self):
        os.chdir(self.original_dir)
        self.test_dir.cleanup()

    def test_process_submissions_and_generate_reports_tc01(self):
        with open("submissions/submission_student_123.txt", "w") as f:
            f.write("27")
        process_submissions_and_generate_reports({"123": "s1@os.edu"})
        self.assertEqual(os.path.exists("reports/report_student_123.html"), True)

    def test_process_submissions_and_generate_reports_tc02(self):
        with open("submissions/submission_student_123.txt", "w") as f:
            f.write("27")
        with open("submissions/submission_student_234.txt", "w") as f:
            f.write("28")
        process_submissions_and_generate_reports({"123": "s1@os.edu", "234": "s2@os.edu"})
        self.assertEqual(os.path.exists("reports/report_student_123.html") and os.path.exists("reports/report_student_234.html"), True)

    def test_process_submissions_and_generate_reports_tc03(self):
        process_submissions_and_generate_reports({})
        self.assertEqual(len(os.listdir("reports")), 0)

    def test_process_submissions_and_generate_reports_tc04(self):
        process_submissions_and_generate_reports("{abx")
        self.assertEqual(len(os.listdir("reports")), 0)


if __name__ == '__main__':
    unittest.main()
