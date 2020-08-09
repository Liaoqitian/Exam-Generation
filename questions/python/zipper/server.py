import prairielearn as pl
import random, copy, math
import base64

def generate(data):
    data["correct_answers"]["solution_one"] = "b == ''"
    data["correct_answers"]["solution_two"] = "a"
    data["correct_answers"]["solution_three"] = "a[0] < b[0]"
    data["correct_answers"]["solution_four"] = "a[0] + zipper(a[1:],b)"
    data["correct_answers"]["solution_five"] = "b[0] + zipper(a,b[1:])"
    data["correct_answers"]["solution_six"] = "reduce(zipper, words)"

def grade(data):
    solution_one = ['b == ""', "b == ''"]
    solution_two = ["a"]
    solution_three = ["a[0] < b[0]", "b[0] > a[0]"]
    solution_four = ["a[0] + zipper(a[1:],b)", "zipper(a[1:],b) + a[0]", "a[0] + zipper(b,a[1:])", "zipper(b,a[1:]) + a[0]"]
    solution_five = ["b[0] + zipper(a,b[1:])", "zipper(a,b[1:]) + b[0]", "b[0] + zipper(b[1:],a)", "zipper(b[1:],a) + b[0]"]
    solution_six = ["reduce(zipper, words)"]

    if data["score"] != 1: 
        if data['submitted_answers']["solution_one"] in solution_one:
            data["partial_scores"]["solution_one"]["score"] = 1
            data["score"] += 0.15
        if data['submitted_answers']["solution_two"] in solution_two:
            data["partial_scores"]["solution_two"]["score"] = 1
            data["score"] += 0.15
        if data['submitted_answers']["solution_three"] in solution_three:
            data["partial_scores"]["solution_three"]["score"] = 1
            data["score"] += 0.15
        if data['submitted_answers']["solution_four"] in solution_four:
            data["partial_scores"]["solution_four"]["score"] = 1
            data["score"] += 0.15
        if data['submitted_answers']["solution_five"] in solution_five:
            data["partial_scores"]["solution_five"]["score"] = 1
            data["score"] += 0.15
        if data['submitted_answers']["solution_six"] in solution_six:
            data["partial_scores"]["solution_six"]["score"] = 1
            data["score"] += 0.25