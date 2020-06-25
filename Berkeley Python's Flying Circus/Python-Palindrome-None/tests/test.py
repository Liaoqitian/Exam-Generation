from pl_helpers import name, points, not_repeated
from pl_unit_test import PLTestCaseWithPlot, PLTestCase
from code_feedback import Feedback
from functools import wraps
import numpy as np
import numpy.random


class Test(PLTestCase):
    @points(0.5)
    @name('Check isPalindromeNone()')
    def test_0(self):
        user_val = Feedback.call_user(self.st.isPalindromeNone, '')
        if Feedback.check_scalar("isPalindromeNone('')", self.ref.isPalindromeNone(''), user_val):
            Feedback.set_score(1)
        else:
            Feedback.set_score(0)

    @points(0.5)
    @name('Check isPalindromeNone(a)')
    def test_1(self):
        user_val = Feedback.call_user(self.st.isPalindromeNone, 'a')
        if Feedback.check_scalar("isPalindromeNone('a')", self.ref.isPalindromeNone('a'), user_val):
            Feedback.set_score(1)
        else:
            Feedback.set_score(0)

    @points(1)
    @name('Check isPalindromeNone(peek)')
    def test_2(self):
        user_val = Feedback.call_user(self.st.isPalindromeNone, 'peek')
        if Feedback.check_scalar("isPalindromeNone('peek')", self.ref.isPalindromeNone('peek'), user_val):
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
            correct_val = self.ref.isPalindromeNone(s)
            user_val = Feedback.call_user(self.st.isPalindromeNone, s)
            if Feedback.check_scalar(f"isPalindromeNone({s})", correct_val, user_val):
                points += 1
        if points <= 5:
            points = 0 
        Feedback.set_score(points / num_tests)