import prairielearn as pl
import random, copy, math, string

def randomString(stringLength=5):
    letters = string.ascii_letters
    return ''.join(random.sample(letters, stringLength))

def generate(data):
    # Randomly create start_index string of length 5.This will be the solution
    solution = randomString(5)

    # Sample the starting and ending point
    start_index = random.randint(1, 3)
    end_index = start_index + 2

    # Compute the solution. 
    output = solution[start_index:end_index]

    # Store the parameters 
    data["correct_answers"]['solution'] = solution
    data['params']['start_index'] = start_index
    data['params']['end_index'] = end_index
    data['params']['output'] = output

def find_duplicate(s): 
    dict = {} 
    for elem in s:
        if elem in dict: 
            return elem 
        dict[elem] = 1
    return 

def grade(data):
    if data["submitted_answers"]["solution"] not in data["format_errors"]: # check we don't already have a format error
        if len(data["submitted_answers"]["solution"]) != 5:
            feedback = "Only a 5-character string is allowed."
            data["format_errors"]["solution"] = feedback
            data["feedback"]["solution"] = feedback
            return
        if len(set(data["submitted_answers"]["solution"])) != 5: 
            duplicated_character = find_duplicate(data["submitted_answers"]["solution"])
            feedback = "Only strings with unique characters are allowed. You have too many " + str(duplicated_character) + "'s."
            data["format_errors"]["solution"] = feedback
            data["feedback"]["solution"] = feedback
            return
    if data['score'] == 0: 
        if data["submitted_answers"]["solution"][data['params']['start_index']:data['params']['end_index']] == data['params']['output']:
            data["partial_scores"]["score"] = 1
            data['score'] = 1
        else:
            # data["partial_scores"]["solution"] = 0
            data["feedback"]["solution"] = "you got this wrong, sorry"