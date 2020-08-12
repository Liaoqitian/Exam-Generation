from pl_helpers import name, points, not_repeated
from pl_unit_test import PLTestCaseWithPlot, PLTestCase
from code_feedback import Feedback
from functools import wraps
import numpy as np
import numpy.random


class Test(PLTestCase):
    @points(1)
    @name('Check find_GC({1:10, 2:10, 3:11}, {10:100, 12:200})')
    def test_0(self):
        user_val = Feedback.call_user(self.st.find_GC, {1:10,2:10,3:11}, {10:100, 12:200})
        if self.ref.find_GC({1:10, 2:10, 3:11}, {10:100, 12:200}) == self.st.find_GC({1:10, 2:10, 3:11}, {10:100, 12:200}):
            Feedback.set_score(1)
        else:
            Feedback.set_score(0)

    @points(1)
    @name('Check find_GC({},{0:10})')
    def test_1(self):
        user_val = Feedback.call_user(self.st.find_GC, {12:140,19:199,21:192}, {166:1200, 195:1300})
        if self.ref.find_GC({12:140,19:199,21:192}, {166:1200, 195:1300}) == user_val:
            Feedback.set_score(1)
        else:
            Feedback.set_score(0)

    @points(2)
    @name('Check find_GC({1:10, 2:10, 3:11, 4:11, 5:12, 6:12}, {10:100, 11:150, 12:200, 13:200})')
    def test_2(self):
        user_val = Feedback.call_user(self.st.find_GC, {1:10, 2:10, 3:11, 4:11, 5:12, 6:12}, {10:100, 11:150, 12:200, 13:200})
        if self.ref.find_GC({1:10, 2:10, 3:11, 4:11, 5:12, 6:12}, {10:100, 11:150, 12:200, 13:200}) == user_val:
            Feedback.set_score(1)
        else:
            Feedback.set_score(0)

    @points(2)
    @name('Check find_GC({1:10, 2:10, 3:11, 4:11, 5:12, 6:12}, {13:200, 14:200})')
    def test_3(self):
        user_val = Feedback.call_user(self.st.find_GC, {1:10, 2:10, 3:11, 4:11, 5:12, 6:12}, {13:200, 14:200})
        if self.ref.find_GC({1:10, 2:10, 3:11, 4:11, 5:12, 6:12}, {13:200, 14:200}) == user_val:
            Feedback.set_score(1)
        else:
            Feedback.set_score(0)
            
    @points(2)
    @name('Check find_GC({1:100, 2:100, 3:100, 4:100}, {100:500, 200:600})')
    def test_4(self):
        user_val = Feedback.call_user(self.st.find_GC, {1:100, 2:100, 3:100, 4:100}, {10:100, 12:200})
        if self.ref.find_GC({1:100, 2:100, 3:100, 4:100}, {10:100, 12:200}) == user_val:
            Feedback.set_score(1)
        else:
            Feedback.set_score(0)

    @points(2)
    @name('Check find_GC({1:100, 2:100, 3:200, 4:200, 5:300, 6:300}, {100:1000, 200:2000, 300:3000, 400:4000})')
    def test_5(self):
        user_val = Feedback.call_user(self.st.find_GC, {1:100, 2:100, 3:200, 4:200, 5:300, 6:300}, {100:1000, 200:2000, 300:3000, 400:4000})
        if self.ref.find_GC({1:100, 2:100, 3:200, 4:200, 5:300, 6:300}, {100:1000, 200:2000, 300:3000, 400:4000}) == user_val:
            Feedback.set_score(1)
        else:
            Feedback.set_score(0)