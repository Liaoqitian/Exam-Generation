from pl_helpers import name, points, not_repeated
from pl_unit_test import PLTestCaseWithPlot, PLTestCase
from code_feedback import Feedback
from functools import wraps
import numpy as np
import numpy.random

class Test(PLTestCase):
    @points(2)
    @name("base case provided by question")
    def test_0(self):
        sp19_enrollment = {"Murtaza": 10, "Lara": 20, "Mansi": 20, "Niki": 15, "Brendan": 10}
        sp19_attendance = {"Murtaza": [10, 9, 10, 10, 10, 2, 9, 10, 9, 1],
                           "Lara": [19, 18, 16, 14, 12, 11, 10, 5, 5, 5],
                           "Mansi": [25, 22, 23, 24, 25, 22, 22, 20, 25, 25],
                           "Niki": [20, 15, 15, 12, 17, 17, 17, 16, 18, 20],
                           "Brendan": [5, 5, 4, 2, 3, 10, 11, 12, 4, 2]}
        user_val = Feedback.call_user(self.st.TAs_with_at_least_half_discussions_full, sp19_enrollment, sp19_attendance)
        if self.ref.TAs_with_at_least_half_discussions_full(sp19_enrollment, sp19_attendance) == user_val:
            Feedback.set_score(1)
        else:
            Feedback.set_score(0)

    @points(4)
    @name('test case 1 (empty list return)')
    def test_1(self):
        enrollment = {"A": 10, "B": 20, "C": 30, "D": 20, "E": 10}
        attendance = {"A": [8, 9, 8, 10, 10, 2, 9, 10, 9, 1], 
                      "B": [19, 18, 16, 14, 12, 11, 10, 5, 5, 5],
                      "C": [25, 22, 23, 24, 25, 22, 22, 20, 25, 25], 
                      "D": [20, 15, 15, 12, 17, 17, 17, 16, 18, 20], 
                      "E": [5, 5, 4, 2, 3, 10, 11, 12, 4, 2]}
        user_val = Feedback.call_user(self.st.TAs_with_at_least_half_discussions_full, enrollment, attendance)
        if self.ref.TAs_with_at_least_half_discussions_full(enrollment, attendance) == user_val:
            Feedback.set_score(1)
        else:
            Feedback.set_score(0)

    @points(4)
    @name('test case 2 (return all)')
    def test_2(self):
        enrollment = {"A": 8, "B": 12, "C": 23, "D": 17, "E": 5}
        attendance = {"A": [8, 9, 8, 10, 10, 2, 6, 7, 3, 1], 
                      "B": [19, 18, 16, 14, 12, 11, 10, 5, 5, 5],
                      "C": [25, 22, 23, 24, 25, 22, 22, 20, 25, 25], 
                      "D": [20, 15, 15, 12, 17, 17, 16, 16, 18, 20], 
                      "E": [5, 5, 4, 2, 3, 10, 11, 12, 4, 2]}
        user_val = Feedback.call_user(self.st.TAs_with_at_least_half_discussions_full, enrollment, attendance)
        if self.ref.TAs_with_at_least_half_discussions_full(enrollment, attendance) == user_val:
            Feedback.set_score(1)
        else:
            Feedback.set_score(0)

    @points(5)
    @name('test case 3 (mix)')
    def test_3(self):
        enrollment = {"A": 8, "B": 12, "C": 23, "D": 17, "E": 5, "Murtaza": 10, "Lara": 20, "Mansi": 20, "Niki": 15, "Brendan": 10, "F": 10, "G": 20, "H": 30, "I": 20, "J": 10}
        attendance = {"A": [8, 9, 8, 10, 10, 2, 6, 7, 3, 1], 
                      "B": [19, 18, 16, 14, 12, 11, 10, 5, 5, 5],
                      "C": [25, 22, 23, 24, 25, 22, 22, 20, 25, 25], 
                      "D": [20, 15, 15, 12, 17, 17, 16, 16, 18, 20], 
                      "E": [5, 5, 4, 2, 3, 10, 11, 12, 4, 2], 
                      "Murtaza": [10, 9, 10, 10, 10, 2, 9, 10, 9, 1],
                      "Lara": [19, 18, 16, 14, 12, 11, 10, 5, 5, 5],
                      "Mansi": [25, 22, 23, 24, 25, 22, 22, 20, 25, 25],
                      "Niki": [20, 15, 15, 12, 17, 17, 17, 16, 18, 20],
                      "Brendan": [5, 5, 4, 2, 3, 10, 11, 12, 4, 2], 
                      "F": [8, 9, 8, 10, 10, 2, 9, 10, 9, 1], 
                      "G": [19, 18, 16, 14, 12, 11, 10, 5, 5, 5],
                      "H": [25, 22, 23, 24, 25, 22, 22, 20, 25, 25], 
                      "I": [20, 15, 15, 12, 17, 17, 17, 16, 18, 20], 
                      "J": [5, 5, 4, 2, 3, 10, 11, 12, 4, 2]}
        user_val = Feedback.call_user(self.st.TAs_with_at_least_half_discussions_full, enrollment, attendance)
        if self.ref.TAs_with_at_least_half_discussions_full(enrollment, attendance) == user_val:
            Feedback.set_score(1)
        else:
            Feedback.set_score(0)