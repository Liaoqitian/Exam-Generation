from pl_helpers import name, points, not_repeated
from pl_unit_test import PLTestCaseWithPlot, PLTestCase
from code_feedback import Feedback
from functools import wraps
import numpy as np
import numpy.random


class Test(PLTestCase):
    @points(2)
    # Basic Test Suites
    @name('Basic Tests')
    def test_0(self):
        points = 0
        num_tests = 3
        test_strings = ['', 'a', 'peak'] 
        for s in test_strings:
            correct_val = self.ref.checkPalindrome(s)
            user_val = Feedback.call_user(self.st.checkPalindrome, s)
            if Feedback.check_scalar(f"checkPalindrome({s})", correct_val, user_val):
                points += 1
        if points < 3: 
            points = 0
        Feedback.set_score(points / num_tests)

    @points(8)
    # Advanced Test Suites
    @name('Advanced Tests')
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