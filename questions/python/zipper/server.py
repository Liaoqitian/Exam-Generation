import prairielearn as pl
import random, copy, math
import base64

def generate(data):
    # There are two variants of the problem: the resulting string is either alphabetically ordered (0) or reversed-ordered (1).
    variant = random.randint(0, 1) 
    data["params"]["variant"] = variant 
    if variant == 1:
        data["params"]["keyword"] = "reverse"
        data["params"]["start"] = "z"
        data["params"]["end"] = "a"
        data["params"]["s1"] = 'zipper("cba", "edc")'
        data["params"]["example_one"] = "edccba"
        data["params"]["s2"] = 'zipper("ecca", "db")'
        data["params"]["example_two"] = "edccba"
    else: 
        data["params"]["keyword"] = ""
        data["params"]["start"] = "a"
        data["params"]["end"] = "z"
        data["params"]["s1"] = 'zipper("abc", "cde")'
        data["params"]["example_one"] = "abccde"
        data["params"]["s2"] = 'zipper("acce", "bd")'
        data["params"]["example_two"] = "abccde"

    text_one = "Fill in the blanks to complete the following recursive function,"
    text_two = "which takes two strings whose letters are in"
    text_three = "sorted order (letters closest to"
    text_four = "always in front of letters closest to"
    text_five = ') and "zips" them together into a single string whose letters are in'
    text_six = "sorted order. There may be duplicates in the input and output." 
    data["params"]["text_one"] = text_one
    data["params"]["text_two"] = text_two
    data["params"]["text_three"] = text_three
    data["params"]["text_four"] = text_four
    data["params"]["text_five"] = text_five
    data["params"]["text_six"] = text_six

    data["correct_answers"]["solution_one"] = "b == ''"
    data["correct_answers"]["solution_two"] = "a"
    data["correct_answers"]["solution_three"] = "a[0] < b[0]"
    data["correct_answers"]["solution_six"] = "reduce(zipper, words)"
    if data["params"]["variant"] == 0: 
        data["correct_answers"]["solution_four"] = "a[0] + zipper(a[1:],b)"
        data["correct_answers"]["solution_five"] = "b[0] + zipper(a,b[1:])"
    else:
        data["correct_answers"]["solution_four"] = "b[0] + zipper(a,b[1:])"
        data["correct_answers"]["solution_five"] = "a[0] + zipper(a[1:],b)"

def grade(data):
    solution_one = ['b == ""', "b == ''"]
    solution_two = ["a"]
    solution_three = ["a[0] < b[0]", "b[0] > a[0]", "a[0] <= b[0]", "b[0] >= a[0]"]
    solution_six = ["reduce(zipper, words)"]
    if data["params"]["variant"] == 0: 
        solution_four = ["a[0] + zipper(a[1:],b)", "a[0] + zipper(b,a[1:])"]
        solution_five = ["b[0] + zipper(a,b[1:])", "b[0] + zipper(b[1:],a)"]
    else: 
        solution_four = ["b[0] + zipper(a,b[1:])", "b[0] + zipper(b[1:],a)"]
        solution_five = ["a[0] + zipper(a[1:],b)", "a[0] + zipper(b,a[1:])"]

    if data["partial_scores"]["solution_one"]["score"] != 1: 
        if data['submitted_answers']["solution_one"] in solution_one:
            data["partial_scores"]["solution_one"]["score"] = 1
            data["score"] += 0.15
    if data["partial_scores"]["solution_two"]["score"] != 1: 
        if data['submitted_answers']["solution_two"] in solution_two:
            data["partial_scores"]["solution_two"]["score"] = 1
            data["score"] += 0.15
    if data["partial_scores"]["solution_three"]["score"] != 1: 
        if data['submitted_answers']["solution_three"] in solution_three:
            data["partial_scores"]["solution_three"]["score"] = 1
            data["score"] += 0.15
    if data["partial_scores"]["solution_four"]["score"] != 1:
        if data['submitted_answers']["solution_four"] in solution_four:
            data["partial_scores"]["solution_four"]["score"] = 1
            data["score"] += 0.15
    if data["partial_scores"]["solution_five"]["score"] != 1:
        if data['submitted_answers']["solution_five"] in solution_five:
            data["partial_scores"]["solution_five"]["score"] = 1
            data["score"] += 0.15
    if data["partial_scores"]["solution_six"]["score"] != 1:
        if data['submitted_answers']["solution_six"] in solution_six:
            data["partial_scores"]["solution_six"]["score"] = 1
            data["score"] += 0.25