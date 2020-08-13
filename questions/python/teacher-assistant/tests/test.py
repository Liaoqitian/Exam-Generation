from pl_helpers import name, points, not_repeated
from pl_unit_test import PLTestCaseWithPlot, PLTestCase
from code_feedback import Feedback
from functools import wraps
import numpy as np
import numpy.random

class Test(PLTestCase):
    @points(0.5)
    @name("base case provided by question")
    def test_0(self):
        sp19_enrollment = {"Murtaza": 10, "Lara": 20, "Mansi":20, "Niki":15, "Brendan": 10}
        sp19_attendance = {"Murtaza": [10, 9, 10, 10, 10, 2, 9, 10, 9, 1],
                           "Lara": [19, 18, 16, 14, 12, 11, 10, 5, 5, 5],
                           "Mansi": [25, 22, 23, 24, 25, 22, 22, 20, 25, 25],
                           "Niki": [20, 15, 15, 12, 17, 17, 17, 16, 18, 20],
                           "Brendan": [ 5, 5, 4, 2, 3, 10, 11, 12, 4, 2]}
        user_val = Feedback.call_user(self.st.TAs_with_at_least_half_discussions_full, sp19_enrollment, sp19_attendance)
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