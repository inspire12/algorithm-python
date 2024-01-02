from unittest import TestCase
from palindrome import isPalindrome, test_solve


class Test(TestCase):

    def test_solve_case_1(self):
        s = "A man, a plan, a canal: Panama"
        value = test_solve(s)
        self.assertTrue(value)

    def test_solve_case_2(self):
        s = "race a car"
        value = test_solve(s)
        self.assertFalse(value)
    def test_solve_case_3(self):
        s = " "
        value = test_solve(s)
        self.assertTrue(value)

    def test_solve_case_4(self):
        s = ".,"
        value = test_solve(s)
        self.assertTrue(value)