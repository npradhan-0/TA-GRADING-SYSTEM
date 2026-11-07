import sys
import os
import tarfile
import unittest
import tempfile

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from main import create_tarball


class test_create_tarball(unittest.TestCase):

    def setUp(self):
        self.test_dir = tempfile.TemporaryDirectory()
        self.original_dir = os.getcwd()
        os.chdir(self.test_dir.name)

        os.makedirs("submissions", exist_ok=True)
        os.makedirs("reports", exist_ok=True)

        with open("index.html", "w") as f:
            f.write("<html></html>")

    def tearDown(self):
        os.chdir(self.original_dir)
        self.test_dir.cleanup()

    def test_create_tarball_tf01(self):
        create_tarball()
        self.assertEqual(os.path.exists("reports_and_submissions.tar.gz"), True)

    def test_create_tarball_tf02(self):
        with open("reports_and_submissions.tar.gz", "w") as f:
            f.write("abcd123")

        create_tarball()
        self.assertEqual(os.path.exists("reports_and_submissions.tar.gz"), True)
        self.assertEqual(tarfile.is_tarfile("reports_and_submissions.tar.gz"), True)


if __name__ == '__main__':
    unittest.main()