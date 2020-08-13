from pl_helpers import name, points, not_repeated
from pl_unit_test import PLTestCaseWithPlot, PLTestCase
from code_feedback import Feedback
from functools import wraps
import numpy as np
import random

class Test(PLTestCase):
    @points(1)
    @name("Base case 1 provided by the question")
    def test_0(self):
        sequence = [1, 2, 3, 3, 4, 4, 6, 4, 4, 5, 5, 5, 5]
        if self.ref.function == "most_common":
            user_val = Feedback.call_user(self.st.most_common, sequence)
            if self.ref.most_common(sequence) == user_val:
                Feedback.set_score(1)
            else:
                Feedback.set_score(0)
        elif self.ref.function == "least_common":
            user_val = Feedback.call_user(self.st.least_common, sequence)
            if self.ref.least_common(sequence) == user_val:
                Feedback.set_score(1)
            else:
                Feedback.set_score(0)
        
    @points(1)
    @name("Base case 2 provided by the question")
    def test_1(self):
        sequence = "uc berkeley also cal"
        if self.ref.function == "most_common":
            user_val = Feedback.call_user(self.st.most_common, sequence)
            if self.ref.most_common(sequence) == user_val:
                Feedback.set_score(1)
            else:
                Feedback.set_score(0)
        elif self.ref.function == "least_common":
            user_val = Feedback.call_user(self.st.least_common, sequence)
            if self.ref.least_common(sequence) == user_val:
                Feedback.set_score(1)
            else:
                Feedback.set_score(0)

    @points(2)
    @name("test 1 (all unique elements list)")
    def test_2(self):
        sequence = [1, 2, 3, 4, 5, 6, 7, 8]
        if self.ref.function == "most_common":
            user_val = Feedback.call_user(self.st.most_common, sequence)
            if self.ref.most_common(sequence) == user_val:
                Feedback.set_score(1)
            else:
                Feedback.set_score(0)
        elif self.ref.function == "least_common":
            user_val = Feedback.call_user(self.st.least_common, sequence)
            if self.ref.least_common(sequence) == user_val:
                Feedback.set_score(1)
            else:
                Feedback.set_score(0)

    @points(2)
    @name("test 2 (all unique elements string)")
    def test_3(self):
        sequence = "sphinxofquartz"
        if self.ref.function == "most_common":
            user_val = Feedback.call_user(self.st.most_common, sequence)
            if self.ref.most_common(sequence) == user_val:
                Feedback.set_score(1)
            else:
                Feedback.set_score(0)
        elif self.ref.function == "least_common":
            user_val = Feedback.call_user(self.st.least_common, sequence)
            if self.ref.least_common(sequence) == user_val:
                Feedback.set_score(1)
            else:
                Feedback.set_score(0)
            
    @points(4)
    @name("test 3")
    def test_4(self):
        sequence = []
        for i in range(20):
            sequence += [random.randint(0, 20)]
        if self.ref.function == "most_common":
            user_val = Feedback.call_user(self.st.most_common, sequence)
            if self.ref.most_common(sequence) == user_val:
                Feedback.set_score(1)
            else:
                Feedback.set_score(0)
        elif self.ref.function == "least_common":
            user_val = Feedback.call_user(self.st.least_common, sequence)
            if self.ref.least_common(sequence) == user_val:
                Feedback.set_score(1)
            else:
                Feedback.set_score(0)