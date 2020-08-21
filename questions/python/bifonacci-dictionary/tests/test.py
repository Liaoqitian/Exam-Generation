from pl_helpers import name, points, not_repeated
from pl_unit_test import PLTestCaseWithPlot, PLTestCase
from code_feedback import Feedback
from functools import wraps
import numpy as np
import numpy.random


class Test(PLTestCase):

    def check(self, user_dict, correct_dict):
        if not isinstance(user_dict, dict) or len(user_dict) != len(correct_dict): 
            Feedback.set_score(0)
            return False
        for key in correct_dict: 
            if key not in user_dict or correct_dict[key] != user_dict[key]:
                Feedback.set_score(0)
                return False
        return True 

    @points(0.5)
    @name('Check bif_dict(1)')
    def test_0(self):
        user_dict = Feedback.call_user(self.st.bif_dict, 1)
        correct_dict = self.ref.bif_dict(1)
        if self.check(user_dict, correct_dict):
            Feedback.set_score(1)
        else:
            Feedback.set_score(0)

    @points(0.5)
    @name('Check bif_dict(2)')
    def test_1(self):
        user_dict = Feedback.call_user(self.st.bif_dict, 2)
        correct_dict = self.ref.bif_dict(2)
        if self.check(user_dict, correct_dict):
            Feedback.set_score(1)
        else:
            Feedback.set_score(0)

    @points(1)
    @name('Check bif_dict(7)')
    def test_2(self):
        user_dict = Feedback.call_user(self.st.bif_dict, 7)
        correct_dict = self.ref.bif_dict(7)
        if self.check(user_dict, correct_dict):
            Feedback.set_score(1)
        else:
            Feedback.set_score(0)

    @points(8)
    @name('Check random values')
    def test_3(self):
        points = 0
        num_tests = 8
        test_values = np.random.choice(np.arange(6, 20), size = num_tests, replace = False)
        for value in test_values:
            user_dict = Feedback.call_user(self.st.bif_dict, value)
            correct_dict = self.ref.bif_dict(value)
            if self.check(user_dict, correct_dict):
                points += 1
        Feedback.set_score(points / num_tests)