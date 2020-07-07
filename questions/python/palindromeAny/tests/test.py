from pl_helpers import name, points, not_repeated
from pl_unit_test import PLTestCaseWithPlot, PLTestCase
from code_feedback import Feedback
from functools import wraps
import numpy as np
import numpy.random


class Test(PLTestCase):
    @points(0.5)
    @name('Check isPalindromeAny()')
    def test_0(self):
        user_val = Feedback.call_user(self.st.isPalindromeAny, '')
        if Feedback.check_scalar("isPalindromeAny('')", self.ref.isPalindromeAny(''), user_val):
            Feedback.set_score(1)
        else:
            Feedback.set_score(0)

    @points(0.5)
    @name('Check isPalindromeAny(a)')
    def test_1(self):
        user_val = Feedback.call_user(self.st.isPalindromeAny, 'a')
        if Feedback.check_scalar("isPalindromeAny('a')", self.ref.isPalindromeAny('a'), user_val):
            Feedback.set_score(1)
        else:
            Feedback.set_score(0)

    @points(1)
    @name('Check isPalindromeAny(peek)')
    def test_2(self):
        user_val = Feedback.call_user(self.st.isPalindromeAny, 'peek')
        if Feedback.check_scalar("isPalindromeAny('peek')", self.ref.isPalindromeAny('peek'), user_val):
            Feedback.set_score(1)
        else:
            Feedback.set_score(0)

    @points(10)
    @name('Check several strings')
    def test_3(self):
        points = 0
        num_tests = 10
        test_strings = ['abc', 'c al', 'aabb', 'abcdefghi', 'palindrome', 'abbba', 'abcba', 'abca', 'refer', 'berkeley']
        for s in test_strings:
            correct_val = self.ref.isPalindromeAny(s)
            user_val = Feedback.call_user(self.st.isPalindromeAny, s)
            if Feedback.check_scalar(f"isPalindromeAny({s})", correct_val, user_val):
                points += 1
        if points <= 5:
            points = 0 
        Feedback.set_score(points / num_tests)