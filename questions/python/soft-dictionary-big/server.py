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

def contains(list_of_strings, answer):
    for string in list_of_strings:
        if string in answer:
            return True 
    return False 

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

    solution_one_low_key_condition = ["key_low <= key", "key >= key_low"]
    solution_one_high_key_condition = ["key < key_high", "key_high > key"]

    solution_three = ['    print("ERROR: no range contains key!")']

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

    solution_four_low_key_condition = ["key_low < high", "high > key_low"] 
    solution_four_high_key_condition = ["low < key_high", "key_high > low"] 

    if data["score"] != 1: 
        ### Grades the first blank
        if data['submitted_answers']["solution_one"] in solution_one:
            data["partial_scores"]["solution_one"]["score"] = 1
            data["score"] += 0.2
        else: 
            if contains(solution_one_low_key_condition, data['submitted_answers']['solution_one']):
                data['partial_scores']["solution_one"]["score"] = 0.4
                data["score"] += 0.08
            if contains(solution_one_high_key_condition, data['submitted_answers']['solution_one']):
                data['partial_scores']["solution_one"]["score"] = 0.4
                data["score"] += 0.08

        ### Grades the third blank
        ### Checks the number of blanks
        count_blanks = 0
        if data["submitted_answers"]["solution_three_one"] == "": 
            count_blanks += 1
        if data["submitted_answers"]["solution_three_two"] == "": 
            count_blanks += 1
        if data["submitted_answers"]["solution_three_three"] == "": 
            count_blanks += 1
        if data["submitted_answers"]["solution_three_four"] == "": 
            count_blanks += 1
        if data["submitted_answers"]["solution_three_five"] == "": 
            count_blanks += 1
        if count_blanks != 4: 
            non_blank = 5 - count_blanks
            error_msg = "Invalid solution! You should at least and only fill in one of the blanks! You currently filled in " + str(non_blank) + " blanks."
            data["format_errors"]['solution_three_one'] = error_msg
            data["format_errors"]['solution_three_two'] = error_msg
            data["format_errors"]['solution_three_three'] = error_msg
            data["format_errors"]['solution_three_four'] = error_msg
            data["format_errors"]['solution_three_five'] = error_msg

        ### Checks the number of spaces 
        number_spaces_one = countBlankSpaces(data['submitted_answers']['solution_three_one'])
        if (number_spaces_one % 4 != 0):
            data['format_errors']['solution_three_one'] = "You have " + str(number_spaces_one) + " spaces. Please make the number of spaces a multiple of 4!"
            
        number_spaces_two = countBlankSpaces(data['submitted_answers']['solution_three_two'])
        if (number_spaces_two % 4 != 0):
            data['format_errors']['solution_three_two'] = "You have " + str(number_spaces_two) + " spaces. Please make the number of spaces a multiple of 4!"

        number_spaces_three = countBlankSpaces(data['submitted_answers']['solution_three_three'])
        if (number_spaces_three % 4 != 0):
            data['format_errors']['solution_three_three'] = "You have " + str(number_spaces_three) + " spaces. Please make the number of spaces a multiple of 4!"

        number_spaces_four = countBlankSpaces(data['submitted_answers']['solution_three_four'])
        if (number_spaces_four % 4 != 0):
            data['format_errors']['solution_three_four'] = "You have " + str(number_spaces_four) + " spaces. Please make the number of spaces a multiple of 4!"

        number_spaces = countBlankSpaces(data['submitted_answers']['solution_three_five'])
        if (number_spaces % 4 != 0):
            data['format_errors']['solution_three_five'] = "You have " + str(number_spaces) + " spaces. Please make the number of spaces a multiple of 4!"
        else: 
            if number_spaces != 4: 
                data["partial_scores"]["solution_three_one"]["score"] = 0
                data["partial_scores"]["solution_three_two"]["score"] = 0
                data["partial_scores"]["solution_three_three"]["score"] = 0
                data["partial_scores"]["solution_three_four"]["score"] = 0
                data["partial_scores"]["solution_three_five"]["score"] = 0
            elif data['submitted_answers']['solution_three_five'][4] == 'p': 
                data['partial_scores']["solution_three_five"]["score"] = 1
                data["score"] += 0.2
        
        if data['submitted_answers']["solution_four"] in solution_four: 
            data["partial_scores"]["solution_four"]["score"] = 1
            data["score"] += 0.4
        else:
            if contains(solution_four_low_key_condition, data['submitted_answers']['solution_four']):
                data['partial_scores']["solution_four"]["score"] = 0.4
                data["score"] += 0.16
            if contains(solution_four_high_key_condition, data['submitted_answers']['solution_four']):
                data['partial_scores']["solution_four"]["score"] = 0.4
                data["score"] += 0.16

def countBlankSpaces(submitted_answer): 
    count = 0
    for char in submitted_answer: 
        if char == ' ':
            count += 1
        else: 
            break 
    return count 
    