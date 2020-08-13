import prairielearn as pl
import pandas as pd
import random

def generate(data): 
    fee = random.randint(3, 6)
    friend_fee = random.randint(1, 2)
    money = [100, 150, 200, 250, 300, 350, 400]
    deposit = [20, 30, 40, 50]
    withdrawal = [10, 15, 25, 35]
    initial_balance = money[random.randint(0, 6)]
    a_deposit = deposit[random.randint(0, 3)]
    b_deposit = deposit[random.randint(0, 3)]
    a_withdrawal = withdrawal[random.randint(0, 3)]

    balance_one = initial_balance + a_deposit - fee 
    balance_two = balance_one - a_withdrawal - fee
    balance_three = balance_two - a_withdrawal - friend_fee
    balance_four = initial_balance + b_deposit
    balance_five = balance_three + 1000 - friend_fee

    data["params"]["fee"] = fee
    data["params"]["friend_fee"] = friend_fee
    data["params"]["initial_balance"] = initial_balance
    data["params"]["a_deposit"] = a_deposit
    data["params"]["b_deposit"] = b_deposit
    data["params"]["a_withdrawal"] = a_withdrawal

    data["params"]["balance_one"] = balance_one
    data["params"]["balance_two"] = balance_two
    data["params"]["balance_three"] = balance_three
    data["params"]["balance_four"] = balance_four
    data["params"]["balance_five"] = balance_five

    data["correct_answers"]["solution_one"] = str(fee)
    data["correct_answers"]["solution_two"] = "self.balance = balance"
    data["correct_answers"]["solution_three"] = "self.balance = self.balance + amount - self.fee"
    data["correct_answers"]["solution_four"] = "self.balance - amount - self.fee"
    data["correct_answers"]["solution_five"] = "self.balance = new_balance"
    data["correct_answers"]["solution_six"] = "a.fee = " + str(friend_fee)
    data["correct_answers"]["solution_seven"] = "Account.fee = 0"
    data["correct_answers"]["solution_eight"] = str(balance_five)

def grade(data):
    solution_three = ["self.balance = self.balance + amount - self.fee", 
                      "self.balance += amount - self.fee", 
                      "self.balance = self.balance - self.fee + amount", 
                      "self.balance -= self.fee - amount",
                      "self.balance = amount + self.balance - self.fee"]
    solution_four = ["self.balance - amount - self.fee", 
                     "self.balance - self.fee - amount"]
    
    if data["partial_scores"]["solution_three"]["score"] != 1: 
        if data['submitted_answers']["solution_three"] in solution_three:
            data["partial_scores"]["solution_three"]["score"] = 1
            data["score"] += 0.12
    if data["partial_scores"]["solution_four"]["score"] != 1:
        if data['submitted_answers']["solution_four"] in solution_four:
            data["partial_scores"]["solution_four"]["score"] = 1
            data["score"] += 0.12