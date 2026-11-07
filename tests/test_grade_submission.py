import sys
import os
import unittest

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from main import grade_submission

class test_grade_submission(unittest.TestCase):
    def test_grade_submission_tc01(self):
        score, _ = grade_submission("27")
        self.assertEqual(score, 4)

    def test_grade_submission_tc02(self):
        score, _ = grade_submission("-9")
        self.assertEqual(score, 4)

    def test_grade_submission_tc03(self):
        score, _ = grade_submission("0")
        self.assertEqual(score, 4)

    def test_grade_submission_tc04(self):
        score, _ = grade_submission("2.1")
        self.assertEqual(score, 4)

    def test_grade_submission_tc05(self):
        score, _ = grade_submission("-7")
        self.assertEqual(score, 4)

    def test_grade_submission_tc06(self):
        score, _ = grade_submission("$12")
        self.assertEqual(score, 4)

    def test_grade_submission_tc07(self):
        score, _ = grade_submission("$12.98")
        self.assertEqual(score, 4)

    def test_grade_submission_tc08(self):
        score, _ = grade_submission("$12,888.90")
        self.assertEqual(score, 4)

    def test_grade_submission_tc09(self):
        score, _ = grade_submission("$12,888.90")
        self.assertEqual(score, 4)

    def test_grade_submission_tc10(self):
        score, _ = grade_submission("(315) 312-5555")
        self.assertEqual(score, 4)

    def test_grade_submission_tc11(self):
        score, _ = grade_submission("315-312-5555")
        self.assertEqual(score, 4)

    def test_grade_submission_tc12(self):
        score, _ = grade_submission("student@example.com")
        self.assertEqual(score, 4)

    def test_grade_submission_tc13(self):
        score, _ = grade_submission("student@cs.example.edu")
        self.assertEqual(score, 4)

    def test_grade_submission_tc14(self):
        score, _ = grade_submission("first.last@example.com")
        self.assertEqual(score, 4)

    def test_grade_submissionv_tc15(self):
        score, _ = grade_submission("-9/3")
        self.assertEqual(score, 0)

    def test_grade_submission_tc16(self):
        score, _ = grade_submission("9.0.8")
        self.assertEqual(score, 0)

    def test_grade_submission_tc17(self):
        score, _ = grade_submission("$12.90")
        self.assertEqual(score, 4)

    def test_grade_submission_tc18(self):
        score, _ = grade_submission("$12,99.90")
        self.assertEqual(score, 0)

    def test_grade_submission_tc19(self):
        score, _ = grade_submission("first last@example.com")
        self.assertEqual(score, 0)

    def test_grade_submission_tc20(self):
        score, _ = grade_submission("first@@example.com")
        self.assertEqual(score, 0)

    def test_grade_submission_tc21(self):
        score, _ = grade_submission("student@example")
        self.assertEqual(score, 0)

    def test_grade_submission_tc22(self):
        score, _ = grade_submission("(315) 3125555")
        self.assertEqual(score, 0)


    def test_grade_submission_tc23(self):
        score, _ = grade_submission("312-5555")
        self.assertEqual(score, 1)

    def test_grade_submission_tc24(self):
        score, _ = grade_submission("27 27 27")
        self.assertEqual(score, 4)

    def test_grade_submission_tc25(self):
        score, _ = grade_submission("10 20 30 40 50 60")
        self.assertEqual(score, 20)

    def test_grade_submission_tc26(self):
        score, _ = grade_submission("Hello world")
        self.assertEqual(score, 0)

    def test_grade_submission_tc27(self):
        score, _ = grade_submission("27")
        self.assertEqual(score, 4)

    def test_grade_submission_tc28(self):
        score, _ = grade_submission("10 20 30 40 50")
        self.assertEqual(score, 20)

    def test_grade_submission_tc29(self):
        score, _ = grade_submission("27 5.6 student@example.com $20 (330) 263-2000")
        self.assertEqual(score, 20)

    def test_grade_submission_tc30(self):
        score, _ = grade_submission("student123@example.com $12 (315) 312-5555")
        self.assertEqual(score, 12)

    def test_grade_submission_tc31(self):
        score, _ = grade_submission("1.1 2.2 3.3 4.4 5.5")
        self.assertEqual(score, 20)

    def test_grade_submission_tc32(self):
        score, results = grade_submission("1.1 2.2 3.3 4.4 5.5 6.6")
        self.assertEqual(score, 20)
        self.assertEqual(results['decimals']['points'], 20)

    def test_grade_submission_tc33(self):
        score, _ = grade_submission("a@b.com c@d.com e@f.com g@h.com i@j.com")
        self.assertEqual(score, 20)

    def test_grade_submission_tc34(self):
        score, _ = grade_submission("a@b.com c@d.com e@f.com g@h.com i@j.com k@l.com")
        self.assertEqual(score, 20)

    def test_grade_submission_tc35(self):
        score, _ = grade_submission("$1 $2 $3 $4 $5")
        self.assertEqual(score, 20)

    def test_grade_submission_tc36(self):
        score, _ = grade_submission("$1 $2 $3 $4 $5 $6")
        self.assertEqual(score, 20)


    def test_grade_submission_tc37(self):
        score, _ = grade_submission("111-222-3333 222-333-4444 333-444-5555 444-555-6666 555-666-7777")
        self.assertEqual(score, 20)

    def test_grade_submission_tc38(self):
        score, _ = grade_submission("111-222-3333 222-333-4444 333-444-5555 444-555-6666 555-666-7777 666-777-8888")
        self.assertEqual(score, 20)

    def test_grade_submission_tc39(self):
        score, _ = grade_submission("27 28 27 28")
        self.assertEqual(score, 8)

    def test_grade_submission_tc40(self):
        score, _ = grade_submission("10 2.5 test@example.com $9.99 123-456-7890")
        self.assertEqual(score, 20)


    def test_grade_submission_tc41(self):
        score, _ = grade_submission("abc 1a2b nine")
        self.assertEqual(score, 0)

if __name__ == '__main__':
    unittest.main()