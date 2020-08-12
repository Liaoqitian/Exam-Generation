from pl_helpers import name, points, not_repeated
from pl_unit_test import PLTestCaseWithPlot, PLTestCase
from code_feedback import Feedback
from functools import wraps
import numpy as np
import numpy.random


class Test(PLTestCase):
    @points(10)
    # Basic Test Suites
    @name('Basic Tests')
    def test_0(self):
        points = 0
        test_strings = ['', 'a', 'peak', 'abc', 'c al', 'aabb', 'abcdefghi', 'palindrome', 'abbba'] 
        num_tests = len(test_strings)
        for s in test_strings:
            correct_val = self.ref.checkPalindrome(s)
            user_val = True
            if self.ref.function == 'is_palindrome_all':
                user_val = Feedback.call_user(self.st.is_palindrome_all, s)
            elif self.ref.function == 'is_palindrome_any':
                user_val = Feedback.call_user(self.st.is_palindrome_any, s)
            else: 
                user_val = Feedback.call_user(self.st.is_palindrome_none, s)
            if Feedback.check_scalar(f"checkPalindrome({s})", correct_val, user_val):
                points += 1
        if points < 3: 
            points = 0
        Feedback.set_score(points / num_tests)

    # @points(8)
    # # Advanced Test Suites
    # @name('Advanced Tests')
    # def test_3(self):
    #     points = 0
    #     num_tests = 8
    #     test_strings = ['abc', 'c al', 'aabb', 'abcdefghi', 'palindrome', 'abbba', 'abcba', 'abca', 'refer', 'berkeley', 'abccba', 'abcdedcba']
    #     for s in test_strings:
    #         correct_val = self.ref.checkPalindrome(s)
    #         # if isinstance(correct_val, bool):
    #         user_val = True
    #         if self.ref.function == 'is_palindrome_all':
    #             user_val = Feedback.call_user(self.st.is_palindrome_all, s)
    #         elif self.ref.function == 'is_palindrome_any':
    #             user_val = Feedback.call_user(self.st.is_palindrome_any, s)
    #         else: 
    #             user_val = Feedback.call_user(self.st.is_palindrome_none, s)
    #         if Feedback.check_scalar(f"checkPalindrome({s})", correct_val, user_val):
    #             points += 1
    #     if points <= 5:
    #         points = 0 
    #     Feedback.set_score(points / num_tests)