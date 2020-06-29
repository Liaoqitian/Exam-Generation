from pl_helpers import name, points, not_repeated
from pl_unit_test import PLTestCaseWithPlot, PLTestCase
from code_feedback import Feedback
from functools import wraps
import numpy as np
import numpy.random


class Test(PLTestCase):
    @points(0.5)
    @name('Check checkPalindrome()')
    def test_0(self):
        user_val = Feedback.call_user(self.st.checkPalindrome, '')
        if Feedback.check_scalar("checkPalindrome('')", self.ref.checkPalindrome(''), user_val):
            Feedback.set_score(1)
        else:
            Feedback.set_score(0)

    @points(0.5)
    @name('Check checkPalindrome(a)')
    def test_1(self):
        user_val = Feedback.call_user(self.st.checkPalindrome, 'a')
        if Feedback.check_scalar("checkPalindrome('a')", self.ref.checkPalindrome('a'), user_val):
            Feedback.set_score(1)
        else:
            Feedback.set_score(0)

    @points(1)
    @name('Check checkPalindrome(peak)')
    def test_2(self):
        user_val = Feedback.call_user(self.st.checkPalindrome, 'peak')
        if Feedback.check_scalar("checkPalindrome('peak')", self.ref.checkPalindrome('peak'), user_val):
            Feedback.set_score(1)
        else:
            Feedback.set_score(0)

    @points(8)
    @name('Check several strings')
    def test_3(self):
        points = 0
        num_tests = 8
        test_strings = ['abc', 'c al', 'aabb', 'abcdefghi', 'palindrome', 'abbba', 'abcba', 'abca', 'refer', 'berkeley', 'abccba', 'abcdedcba']
        for s in test_strings:
            correct_val = self.ref.checkPalindrome(s)
            if isinstance(correct_val, bool): 
                user_val = Feedback.call_user(self.st.checkPalindrome, s)
                if Feedback.check_scalar(f"checkPalindrome({s})", correct_val, user_val):
                    points += 1
        if points <= 5:
            points = 0 
        Feedback.set_score(points / num_tests)