from pl_helpers import name, points, not_repeated
from pl_unit_test import PLTestCaseWithPlot, PLTestCase
from code_feedback import Feedback
from functools import wraps
import numpy as np
import numpy.random


class Test(PLTestCase):
    @points(1)
    @name('Check lcs("crows eat yay", "ows eat ")')
    def test_0(self):
        if self.ref.lcs("crows eat yay", "ows eat ") == self.st.lcs("crows eat yay", "ows eat "):
            Feedback.set_score(1)
        else:
            Feedback.set_score(0)

    @points(1)
    @name('Check lcs("pickle", "orcs")')
    def test_1(self):
        if self.ref.lcs("pickle", "orcs") == self.st.lcs("pickle", "orcs"):
            Feedback.set_score(1)
        else:
            Feedback.set_score(0)

    @points(1)
    @name('Check lcs("leetcode", "beet")')
    def test_3(self):
        if self.ref.lcs("leetcode", "beet") == self.st.lcs("leetcode", "beet"):
            Feedback.set_score(1)
        else:
            Feedback.set_score(0)

    @points(1)
    @name('Check lcs("abcd", "efgh")')
    def test_4(self):
        if self.ref.lcs("abcd", "efgh") == self.st.lcs("abcd", "efgh"):
            Feedback.set_score(1)
        else:
            Feedback.set_score(0)

    @points(1)
    @name('Check lcs("computer science", "computer biology")')
    def test_5(self):
        if self.ref.lcs("computer science", "computer biology") == self.st.lcs("computer science", "computer biology"):
            Feedback.set_score(1)
        else:
            Feedback.set_score(0)
