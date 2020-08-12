from pl_helpers import name, points, not_repeated
from pl_unit_test import PLTestCaseWithPlot, PLTestCase
from code_feedback import Feedback
from functools import wraps
import numpy as np
import numpy.random


class Test(PLTestCase):
    @points(1)
    @name('Base case (provided by the question)')
    def test_0(self):
        if self.ref.function == "find_GC": 
            GP = {1:10, 2:10, 3:11}
            PC = {10:100, 12:200}
            user_val = Feedback.call_user(self.st.find_GC, GP, PC)
            if self.ref.find_GC(GP, PC) == user_val:
                Feedback.set_score(1)
            else:
                Feedback.set_score(0)
        
        elif self.ref.function == "same_keys":
            D1 = {1:10, 2:10, 3:11}
            D2 = {1:20, 4:30}
            user_val = Feedback.call_user(self.st.same_keys, D1, D2)
            if self.ref.same_keys(D1, D2) == user_val: 
                Feedback.set_score(1)
            else:
                Feedback.set_score(0)
        
        elif self.ref.function == "same_values": 
            D1 = {1:10, 2:10, 3:11}
            D2 = {1:20, 4:11, 5:10}
            user_val = Feedback.call_user(self.st.same_values, D1, D2)
            if self.ref.same_values(D1, D2) == user_val:
                Feedback.set_score(1)
            else:
                Feedback.set_score(0)

    @points(1)
    @name('No match')
    def test_1(self):
        if self.ref.function == "find_GC": 
            GP = {12:140, 19:199, 21:192}
            PC = {166:1200, 195:1300}
            user_val = Feedback.call_user(self.st.find_GC, GP, PC)
            if self.ref.find_GC(GP, PC) == user_val:
                Feedback.set_score(1)
            else:
                Feedback.set_score(0)
        elif self.ref.function == "same_keys":
            D1 = {1:10, 2:10, 3:10, 4:10}
            D2 = {5:20, 6:20, 7:30, 8:40}
            user_val = Feedback.call_user(self.st.same_keys, D1, D2)
            if self.ref.same_keys(D1, D2) == user_val: 
                Feedback.set_score(1)
            else:
                Feedback.set_score(0)

        elif self.ref.function == "same_values": 
            D1 = {1:10, 2:10, 3:10}
            D2 = {1:15, 2:15, 3:15}
            user_val = Feedback.call_user(self.st.same_values, D1, D2)
            if self.ref.same_values(D1, D2) == user_val:
                Feedback.set_score(1)
            else:
                Feedback.set_score(0)
        

    @points(2)
    @name('Two matches')
    def test_2(self):
        if self.ref.function == "find_GC": 
            GP = {1:10, 2:20, 3:30}
            PC = {10:100, 15:150, 20:200}
            user_val = Feedback.call_user(self.st.find_GC, GP, PC)
            if self.ref.find_GC(GP, PC) == user_val:
                Feedback.set_score(1)
            else:
                Feedback.set_score(0)

        elif self.ref.function == "same_keys":
            D1 = {1:10, 2:10, 3:10, 4:10}
            D2 = {1:20, 2:20, 7:30, 8:40}
            user_val = Feedback.call_user(self.st.same_keys, D1, D2)
            if self.ref.same_keys(D1, D2) == user_val: 
                Feedback.set_score(1)
            else:
                Feedback.set_score(0)

        elif self.ref.function == "same_values": 
            D1 = {1:10, 2:12, 3:11}
            D2 = {1:10, 4:9, 5:10}
            user_val = Feedback.call_user(self.st.same_values, D1, D2)
            if self.ref.same_values(D1, D2) == user_val:
                Feedback.set_score(1)
            else:
                Feedback.set_score(0)

    @points(2)
    @name('More than two matches')
    def test_3(self):
        if self.ref.function == "find_GC": 
            GP = {1:10, 2:10, 3:11, 4:11, 5:12, 6:12}
            PC = {10:100, 11:150, 12:200, 13:200}
            user_val = Feedback.call_user(self.st.find_GC, GP, PC)
            if self.ref.find_GC(GP, PC) == user_val:
                Feedback.set_score(1)
            else:
                Feedback.set_score(0)

        elif self.ref.function == "same_keys":
            D1 = {1:10, 2:10, 3:10, 4:10}
            D2 = {1:20, 2:20, 3:30, 4:40}
            user_val = Feedback.call_user(self.st.same_keys, D1, D2)
            if self.ref.same_keys(D1, D2) == user_val: 
                Feedback.set_score(1)
            else:
                Feedback.set_score(0)

        elif self.ref.function == "same_values": 
            D1 = {1:10, 2:12, 3:11}
            D2 = {1:10, 2:11, 4:11, 5:10}
            user_val = Feedback.call_user(self.st.same_values, D1, D2)
            if self.ref.same_values(D1, D2) == user_val:
                Feedback.set_score(1)
            else:
                Feedback.set_score(0)
            
    @points(2)
    @name('Most complicated case')
    def test_4(self):
        if self.ref.function == "find_GC": 
            GP = {1:10, 2:10, 3:20, 4:20, 5:30, 6:30, 7:30, 8:40, 9:40, 10:50, 11:60}
            PC = {10:100, 20:200, 30:300, 40:400, 70:700, 80:800}
            user_val = Feedback.call_user(self.st.find_GC, GP, PC)
            if self.ref.find_GC(GP, PC) == user_val:
                Feedback.set_score(1)
            else:
                Feedback.set_score(0)

        elif self.ref.function == "same_keys":
            D1 = {1:10, 2:10, 3:10, 4:10, 5:40, 6:70, 7:80}
            D2 = {1:20, 2:20, 3:30, 4:40, 6:90, 9:100}
            user_val = Feedback.call_user(self.st.same_keys, D1, D2)
            if self.ref.same_keys(D1, D2) == user_val: 
                Feedback.set_score(1)
            else:
                Feedback.set_score(0)

        elif self.ref.function == "same_values": 
            D1 = {1:10, 2:12, 3:11, 4:12, 5:13, 6:14, 7:16}
            D2 = {1:10, 2:11, 4:11, 5:12, 6:13, 7:14, 8:15}
            user_val = Feedback.call_user(self.st.same_values, D1, D2)
            if self.ref.same_values(D1, D2) == user_val:
                Feedback.set_score(1)
            else:
                Feedback.set_score(0)

