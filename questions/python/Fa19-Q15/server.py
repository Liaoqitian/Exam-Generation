import prairielearn as pl
import random, copy, math
import base64

def generate(data):
    data["correct_answers"]["solution_one"] = "key_low <= key < key_high:"
    data["correct_answers"]["solution_two"] = "SD[low_high_range]"
    data["correct_answers"]["solution_three_one"] = ""
    data["correct_answers"]["solution_three_two"] = ""
    data["correct_answers"]["solution_three_three"] = ""
    data["correct_answers"]["solution_three_four"] = ""
    data["correct_answers"]["solution_three_five"] = "    print('ERROR: no range contains key!')"
    data["correct_answers"]["solution_four"] = "not(high <= key_low or key_high <= low):"

def grade(data):
    solution_one = ["key_low <= key < key_high:", 
                    "key_high > key >= key_low:",
                    "key_low <= key and key < key_high:", 
                    "key >= key_low and key < key_high:", 
                    "key_low <= key and key_high > key:",
                    "key >= key_low and key_high > key:",
                    "key < key_high and key_low <= key:", 
                    "key_high > key and key_low <= key:", 
                    "key < key_high and key >= key_low:", 
                    "key_high > key and key >= key_low:"
                    "key_low <= key < key_high", 
                    "key_high > key >= key_low",
                    "key_low <= key and key < key_high", 
                    "key >= key_low and key < key_high", 
                    "key_low <= key and key_high > key",
                    "key >= key_low and key_high > key",
                    "key < key_high and key_low <= key", 
                    "key_high > key and key_low <= key", 
                    "key < key_high and key >= key_low", 
                    "key_high > key and key >= key_low"]

    solution_four = ["not(high <= key_low or key_high <= low):", 
                      "key_low < high and low < key_high:", 
                      "high > key_low and low < key_high:",
                      "key_low < high and key_high > low:",
                      "high > key_low and key_high > low:",
                      "low < key_high and key_low < high:", 
                      "key_high > low and key_low < high:", 
                      "low < key_high and high > key_low:",
                      "key_high > low and high > key_low:",
                      "not(high <= key_low or key_high <= low)", 
                      "key_low < high and low < key_high", 
                      "high > key_low and low < key_high",
                      "key_low < high and key_high > low",
                      "high > key_low and key_high > low",
                      "low < key_high and key_low < high", 
                      "key_high > low and key_low < high", 
                      "low < key_high and high > key_low",
                      "key_high > low and high > key_low"]

    if data["score"] != 1: 
        if data['raw_submitted_answers']["solution_one"] in solution_one:
            data["partial_scores"]["solution_one"]["score"] = 1
            data["score"] += 0.2
        if data['submitted_answers']["solution_four"] in solution_four: 
            data["partial_scores"]["solution_four"]["score"] = 1
            data["score"] += 0.4