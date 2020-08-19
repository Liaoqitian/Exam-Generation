import prairielearn as pl
import pandas as pd
import random

def generate(data): 
    parameter_set = [["A", "B"], ["C", "D"], ["S1", "S2"], ["T1", "T2"], ["S", "T"], ["X", "Y"], ["C", "D"]]
    chosen_parameter = parameter_set[random.randint(0, 6)]
    parameter_one = chosen_parameter[0]
    parameter_two = chosen_parameter[1]
    data["params"]["parameter_one"] = parameter_one
    data["params"]["parameter_two"] = parameter_two

    variants = ["twin_remover", "twin_keeper", "twin_counter", "non_twin_counter"]
    function = variants[random.randint(0, 3)]
    data["params"]["introduction"] = "Fill in the blank to complete the following recursive function,"
    data["correct_answers"]["solution_one"] = 'B == ""'
    data["correct_answers"]["solution_three"] = "A[0] == B[0]"
    data["params"]["function"] = function 

    # Case one: Twin Remover
    if function == "twin_remover": 
        data["params"]["description_one"] = """which takes two strings, and "zips" the characters in the strings from left to right together by their indices. If the characters are the"""
        data["params"]["keyword"] = "same"
        data["params"]["description_two"] = """, we skip it. Otherwise, we put the two characters in a tuple and the order of the characters is regardless. The order of the tuples should 
        be the same as the characters in the input strings. The input strings may be of different length. The function should return a list of tuples. """

        data["params"]["ex_one"] = 'twin_remover("abc", "dbe")'
        data["params"]["ex_comments"] = '## The second character in "abc" and "dbe" are both "b", so we skip it.'
        data["params"]["ex_res"] = "[('a', 'd'), ('c', 'e')]" 

        data["params"]["code_line_three"] = "return []"

        data["correct_answers"]["solution_two"] = "[]"
        data["correct_answers"]["solution_four"] = "twin_remover(" + parameter_one + "[1:], " + parameter_two + "[1:])"
        data["correct_answers"]["solution_five"] = "[(" + parameter_one + "[0], " + parameter_two + "[0])] + twin_remover(" + parameter_one + "[1:], " + parameter_two + "[1:])"

    # Case two: Twin Keeper
    elif function == "twin_keeper":
        data["params"]["description_one"] = """which takes two strings, and "zips" the characters in the strings from left to right together by their indices. If the characters are"""
        data["params"]["keyword"] = "different"
        data["params"]["description_two"] = """, we skip it. Otherwise, we put the two characters in a tuple and their order of the characters is regardless. The order of the tuples should 
        be the same as the characters in the input strings. The input strings may be of different length. The function should return a list of tuples. """

        data["params"]["ex_one"] = 'twin_keeper("abc", "dbe")'
        data["params"]["ex_comments"] = '## The second character in "abc" and "dbe" are both "b", so we keep it.'
        data["params"]["ex_res"] = "[('b', 'b')]" 

        data["params"]["code_line_three"] = "return []"

        data["correct_answers"]["solution_two"] = "[]"
        data["correct_answers"]["solution_four"] = "[(" + parameter_one + "[0], " + parameter_two + "[0])] + twin_keeper(" + parameter_one + "[1:], " + parameter_two + "[1:])"
        data["correct_answers"]["solution_five"] = "twin_keeper(" + parameter_one + "[1:], " + parameter_two + "[1:])"

    # Case three: Twin Counter
    elif function == "twin_counter": 
        data["params"]["description_one"] = """which takes two strings, and count the number of"""
        data["params"]["keyword"] = ""
        data["params"]["description_two"] = """matching-character pairs if you "zip" the characters in the strings together by their indices. Recall that "zip" usually returns 
        a list of tuples. A matching-character pair is definded as a tuple whose two elements are the same."""

        data["params"]["ex_one"] = 'twin_counter("abc", "dbe")'
        data["params"]["ex_comments"] = '## The second character in "abc" and "dbe" are both "b", it is a character-matching pair.'
        data["params"]["ex_res"] = "1"

        data["params"]["code_line_three"] = "return 0"
        
        data["correct_answers"]["solution_two"] = "0"
        data["correct_answers"]["solution_four"] = "1 + twin_counter(" + parameter_one + "[1:], " + parameter_two + "[1:])"
        data["correct_answers"]["solution_five"] = "twin_counter(" + parameter_one + "[1:], " + parameter_two + "[1:])"
    
    # Case four: Non Twin Counter
    elif function == "non_twin_counter": 
        data["params"]["description_one"] = """which takes two strings, and count the number of"""
        data["params"]["keyword"] = "non-"
        data["params"]["description_two"] = """matching-character pairs if you "zip" the characters in the strings together by their indices. Recall that "zip" usually returns 
        a list of tuples. A non-matching-character pair is definded as a tuple whose two elements are different. """

        data["params"]["ex_one"] = 'non_twin_counter("abc", "dbe")'
        data["params"]["ex_comments"] = '## Except the second character in "abc" and "dbe" are both "b", the other two pairs are all non-matching-character pairs.'
        data["params"]["ex_res"] = "2"

        data["params"]["code_line_three"] = "return 0"

        data["correct_answers"]["solution_two"] = "0"
        data["correct_answers"]["solution_four"] = "non_twin_counter(" + parameter_one + "[1:], " + parameter_two + "[1:])"
        data["correct_answers"]["solution_five"] = "1 + non_twin_counter(" + parameter_one + "[1:], " + parameter_two + "[1:])"


def grade(data):
    # Accept missing one parentheses as correct
    parameter_one = data["params"]["parameter_one"]
    parameter_two = data["params"]["parameter_two"]

    solution_one = [parameter_two + ' == ""', parameter_two + " == ''", parameter_two + " == '':", parameter_two + ' == "":']
    solution_three = [parameter_one + "[0] == " + parameter_two + "[0]", parameter_two + "[0] == " + parameter_one + "[0]", 
                      parameter_one + "[0] == " + parameter_two + "[0]:", parameter_two + "[0] == " + parameter_one + "[0]:"]
    if data["params"]["function"] == "twin_remover":
        
        solution_four = ["twin_remover(" + parameter_one + "[1:], " + parameter_two + "[1:])", 
                         "twin_remover(" + parameter_two + "[1:], " + parameter_one + "[1:])", 
                         "twin_remover(" + parameter_one + "[1:], " + parameter_two + "[1:]",
                         "twin_remover(" + parameter_two + "[1:], " + parameter_one + "[1:]"]

        solution_five = ["[(" + parameter_one + "[0], " + parameter_two + "[0])] + twin_remover(" + parameter_one + "[1:], " + parameter_two + "[1:])", 
                         "[(" + parameter_two + "[0], " + parameter_one + "[0])] + twin_remover(" + parameter_one + "[1:], " + parameter_two + "[1:])", 
                         "[(" + parameter_one + "[0], " + parameter_two + "[0])] + twin_remover(" + parameter_two + "[1:], " + parameter_one + "[1:])", 
                         "[(" + parameter_two + "[0], " + parameter_one + "[0])] + twin_remover(" + parameter_two + "[1:], " + parameter_one + "[1:])", 
                         "[(" + parameter_one + "[0], " + parameter_two + "[0])] + twin_remover(" + parameter_one + "[1:], " + parameter_two + "[1:]", 
                         "[(" + parameter_two + "[0], " + parameter_one + "[0])] + twin_remover(" + parameter_one + "[1:], " + parameter_two + "[1:]", 
                         "[(" + parameter_one + "[0], " + parameter_two + "[0])] + twin_remover(" + parameter_two + "[1:], " + parameter_one + "[1:]", 
                         "[(" + parameter_two + "[0], " + parameter_one + "[0])] + twin_remover(" + parameter_two + "[1:], " + parameter_one + "[1:]"]

    elif data["params"]["function"] == "twin_keeper":
        solution_four = ["[(" + parameter_one + "[0], " + parameter_two + "[0])] + twin_keeper(" + parameter_one + "[1:], " + parameter_two + "[1:])", 
                         "[(" + parameter_two + "[0], " + parameter_one + "[0])] + twin_keeper(" + parameter_one + "[1:], " + parameter_two + "[1:])", 
                         "[(" + parameter_one + "[0], " + parameter_two + "[0])] + twin_keeper(" + parameter_two + "[1:], " + parameter_one + "[1:])", 
                         "[(" + parameter_two + "[0], " + parameter_one + "[0])] + twin_keeper(" + parameter_two + "[1:], " + parameter_one + "[1:])", 
                         "[(" + parameter_one + "[0], " + parameter_two + "[0])] + twin_keeper(" + parameter_one + "[1:], " + parameter_two + "[1:]", 
                         "[(" + parameter_two + "[0], " + parameter_one + "[0])] + twin_keeper(" + parameter_one + "[1:], " + parameter_two + "[1:]", 
                         "[(" + parameter_one + "[0], " + parameter_two + "[0])] + twin_keeper(" + parameter_two + "[1:], " + parameter_one + "[1:]", 
                         "[(" + parameter_two + "[0], " + parameter_one + "[0])] + twin_keeper(" + parameter_two + "[1:], " + parameter_one + "[1:]"]
        solution_five = ["twin_keeper(" + parameter_one + "[1:], " + parameter_two + "[1:])", 
                         "twin_keeper(" + parameter_two + "[1:], " + parameter_one + "[1:])", 
                         "twin_keeper(" + parameter_one + "[1:], " + parameter_two + "[1:]", 
                         "twin_keeper(" + parameter_two + "[1:], " + parameter_one + "[1:]"]
    
    elif data["params"]["function"] == "twin_counter":
        solution_four = ["1 + twin_counter(" + parameter_one + "[1:], " + parameter_two + "[1:])", 
                         "1 + twin_counter(" + parameter_two + "[1:], " + parameter_one + "[1:])",
                         "twin_counter(" + parameter_one + "[1:], " + parameter_two + "[1:]) + 1",
                         "twin_counter(" + parameter_two + "[1:], " + parameter_one + "[1:]) + 1",
                         "1 + twin_counter(" + parameter_one + "[1:], " + parameter_two + "[1:]", 
                         "1 + twin_counter(" + parameter_two + "[1:], " + parameter_one + "[1:]",
                         "twin_counter(" + parameter_one + "[1:], " + parameter_two + "[1:] + 1",
                         "twin_counter(" + parameter_two + "[1:], " + parameter_one + "[1:] + 1"]
        solution_five = ["twin_counter(" + parameter_one + "[1:], " + parameter_two + "[1:])", 
                         "twin_counter(" + parameter_two + "[1:], " + parameter_one + "[1:])", 
                         "twin_counter(" + parameter_one + "[1:], " + parameter_two + "[1:]", 
                         "twin_counter(" + parameter_two + "[1:], " + parameter_one + "[1:]"]
    
    elif data["params"]["function"] == "non_twin_counter":
        solution_four = ["non_twin_counter(" + parameter_one + "[1:], " + parameter_two + "[1:])", 
                         "non_twin_counter(" + parameter_two + "[1:], " + parameter_one + "[1:])", 
                         "non_twin_counter(" + parameter_one + "[1:], " + parameter_two + "[1:]", 
                         "non_twin_counter(" + parameter_two + "[1:], " + parameter_one + "[1:]"]
        solution_five = ["1 + non_twin_counter(" + parameter_one + "[1:], " + parameter_two + "[1:])", 
                         "1 + non_twin_counter(" + parameter_two + "[1:], " + parameter_one + "[1:])", 
                         "non_twin_counter(" + parameter_one + "[1:], " + parameter_two + "[1:]) + 1", 
                         "non_twin_counter(" + parameter_two + "[1:], " + parameter_one + "[1:]) + 1", 
                         "1 + non_twin_counter(" + parameter_one + "[1:], " + parameter_two + "[1:]", 
                         "1 + non_twin_counter(" + parameter_two + "[1:], " + parameter_one + "[1:]", 
                         "non_twin_counter(" + parameter_one + "[1:], " + parameter_two + "[1:] + 1", 
                         "non_twin_counter(" + parameter_two + "[1:], " + parameter_one + "[1:] + 1"]
    
    if data["partial_scores"]["solution_one"]["score"] != 1: 
        if data['submitted_answers']["solution_one"] in solution_one:
            data["partial_scores"]["solution_one"]["score"] = 1
            data["score"] += 0.05
    if data["partial_scores"]["solution_three"]["score"] != 1: 
        if data['submitted_answers']["solution_three"] in solution_three:
            data["partial_scores"]["solution_three"]["score"] = 1
            data["score"] += 0.1
    if data["partial_scores"]["solution_four"]["score"] != 1:
        if data['submitted_answers']["solution_four"] in solution_four:
            data["partial_scores"]["solution_four"]["score"] = 1
            data["score"] += 0.4
    if data["partial_scores"]["solution_five"]["score"] != 1:
        if data['submitted_answers']["solution_five"] in solution_five:
            data["partial_scores"]["solution_five"]["score"] = 1
            data["score"] += 0.4
    if data["partial_scores"]["solution_four"]["score"] != 1 and data["partial_scores"]["solution_five"]["score"] != 1: 
        if data['submitted_answers']["solution_four"] in solution_five and data['submitted_answers']["solution_five"] in solution_four:
            data["partial_scores"]["solution_four"]["score"] = 0.875
            data["partial_scores"]["solution_five"]["score"] = 0.875
            data["score"] += 0.7

