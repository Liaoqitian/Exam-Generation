import prairielearn as pl
import random, copy, math, string

def generate(data):
    # Randomly create start_index string of length 5.
    def id_generator(size=5, chars = string.ascii_uppercase + string.digits):
        return ''.join(random.choice(chars) for _ in range(size))
    elem = id_generator()

    # Sample the starting and ending point
    start_index = random.randint(1, 3)
    end_index = random.randint(start_index + 1, len(elem) - 1)

    # Compute the solution. 
    solution = elem[start_index : end_index]

    # Store the parameters 
    data['params']['elem'] = elem
    data['params']['start_index'] = start_index
    data['params']['end_index'] = end_index
    data['params']['solution'] = solution

def grade(data):
    if data["submitted_answers"]["solution"] not in data["format_errors"]: # check we don't already have a format error
        if len(data["submitted_answers"]["solution"]) != 5:
            data["format_errors"]["solution"] = "Only a 5-character string is allowed."
            data["feedback"]["solution"] = "Only a 5-character string is allowed."
    if data['score'] == 0: 
        if data["submitted_answers"]["solution"][data['params']['start_index'] : data['params']['end_index']] == data['correct_answers']['solution']:
            data["partial_scores"]["score"] = 1
            data['score'] = 1
            data["feedback"]["solution"] = "you got this correct!"
        else:
            # data["partial_scores"]["solution"] = 0
            data["feedback"]["solution"] = "you got this wrong, sorry"