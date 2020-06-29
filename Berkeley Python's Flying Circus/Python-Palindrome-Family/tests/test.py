from pl_helpers import name, points, not_repeated
from pl_unit_test import PLTestCaseWithPlot, PLTestCase
from code_feedback import Feedback
from functools import wraps
import numpy as np
import numpy.random


class Test(PLTestCase):
    @points(0.5)
    @name('Check isPalindromeAll()')
    def test_0(self):
        user_val = Feedback.call_user(self.st.isPalindromeAll, '')
        if Feedback.check_scalar("isPalindromeAll('')", self.ref.isPalindromeAll(''), user_val):
            Feedback.set_score(1)
        else:
            Feedback.set_score(0)

    @points(0.5)
    @name('Check isPalindromeAll(a)')
    def test_1(self):
        user_val = Feedback.call_user(self.st.isPalindromeAll, 'a')
        if Feedback.check_scalar("isPalindromeAll('a')", self.ref.isPalindromeAll('a'), user_val):
            Feedback.set_score(1)
        else:
            Feedback.set_score(0)

    @points(1)
    @name('Check isPalindromeAll(peak)')
    def test_2(self):
        user_val = Feedback.call_user(self.st.isPalindromeAll, 'peak')
        if Feedback.check_scalar("isPalindromeAll('peak')", self.ref.isPalindromeAll('peak'), user_val):
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
            if s in ans:
                correct_val = self.ref.isPalindromeAll(s)
                user_val = Feedback.call_user(self.st.isPalindromeAll, s)
                if Feedback.check_scalar(f"isPalindromeAll({s})", correct_val, user_val):
                    points += 1
        if points <= 5:
            points = 0 
        Feedback.set_score(points / num_tests)