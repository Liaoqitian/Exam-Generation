from pl_helpers import name, points, not_repeated
from pl_unit_test import PLTestCaseWithPlot, PLTestCase
from code_feedback import Feedback
from functools import wraps
import numpy as np
import numpy.random


class Test(PLTestCase):
    @points(0.5)
    @name('Check nib(0)')
    def test_0(self):
        user_val = Feedback.call_user(self.st.nib, 0)
        if Feedback.check_scalar("nib(0)", self.ref.nib(0), user_val):
            Feedback.set_score(1)
        else:
            Feedback.set_score(0)

    @points(0.5)
    @name('Check nib(1)')
    def test_1(self):
        user_val = Feedback.call_user(self.st.nib, 1)
        if Feedback.check_scalar("nib(1)", self.ref.nib(1), user_val):
            Feedback.set_score(1)
        else:
            Feedback.set_score(0)

    @points(1)
    @name('Check nib(7)')
    def test_2(self):
        user_val = Feedback.call_user(self.st.nib, 7)
        if Feedback.check_scalar("nib(7)", self.ref.nib(7), user_val):
            Feedback.set_score(1)
        else:
            Feedback.set_score(0)

    @points(8)
    @name('Check random values')
    def test_3(self):
        points = 0
        num_tests = 8
        test_values = np.random.choice(np.arange(6, 20), size=num_tests, replace=False)
        for in_val in test_values:
            correct_val = self.ref.nib(in_val)
            user_val = Feedback.call_user(self.st.nib, in_val)
            if Feedback.check_scalar(f"nib({in_val})", correct_val, user_val):
                points += 1
        Feedback.set_score(points / num_tests)