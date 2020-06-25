from pl_helpers import name, points, not_repeated
from pl_unit_test import PLTestCaseWithPlot, PLTestCase
from code_feedback import Feedback
from functools import wraps
import numpy as np
import numpy.random


class Test(PLTestCase):
    @points(0.5)
    @name('Check isPalindrome()')
    def test_0(self):
        user_val = Feedback.call_user(self.st.isPalindrome, '')
        if Feedback.check_scalar("isPalindrome('')", self.ref.isPalindrome(''), user_val):
            Feedback.set_score(1)
        else:
            Feedback.set_score(0)

    @points(0.5)
    @name('Check isPalindrome(a)')
    def test_1(self):
        user_val = Feedback.call_user(self.st.isPalindrome, 'a')
        if Feedback.check_scalar("isPalindrome('a')", self.ref.isPalindrome('a'), user_val):
            Feedback.set_score(1)
        else:
            Feedback.set_score(0)

    @points(1)
    @name('Check isPalindrome(aba)')
    def test_2(self):
        user_val = Feedback.call_user(self.st.isPalindrome, 'aba')
        if Feedback.check_scalar("isPalindrome('aba)", self.ref.isPalindrome('aba'), user_val):
            Feedback.set_score(1)
        else:
            Feedback.set_score(0)

    @points(10)
    @name('Check several strings')
    def test_3(self):
        points = 0
        num_tests = 10
        test_strings = ['abc', 'abca', 'aabb', 'string','palindrome', 'abbba', 'abcba', 'abccba', 'adada', 'abcdedcba']
        for s in test_strings:
            correct_val = self.ref.isPalindrome(s)
            user_val = Feedback.call_user(self.st.isPalindrome, s)
            if Feedback.check_scalar(f"isPalindrome({s})", correct_val, user_val):
                points += 1
        if points <= 5:
            points = 0 
        Feedback.set_score(points / num_tests)