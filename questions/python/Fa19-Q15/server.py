import prairielearn as pl
import random, copy, math
import base64

def generate(data):
    data["correct_answers"]["solution_one"] = "key_low <= key < key_high:"
    data["correct_answers"]["solution_two"] = "SD[low_high_range]"
    data["correct_answers"]["solution_three"] = "not(high <= key_low or key_high <= low):"

def grade(data):
    solution_one = ["key_low <= key < key_high:", "key_low <= key and key < key_high:", "key < key_high and key_low <= key:"]
    solution_three = ["not(high <= key_low or key_high <= low):", "key_low < high and low < key_high:", "low < key_high and key_low < high"]
    if data["score"] != 1: 
        if data['raw_submitted_answers']["solution_one"] in solution_one:
            data["partial_scores"]["solution_one"]["score"] = 1
            data["score"] += 0.4
        if data['submitted_answers']["solution_three"] in solution_three: 
            data["partial_scores"]["solution_three"]["score"] = 1
            data["score"] += 0.4