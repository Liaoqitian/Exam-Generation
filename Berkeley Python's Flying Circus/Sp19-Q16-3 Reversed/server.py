import prairielearn as pl
import random, copy, math, string

def randomString(stringLength=5):
    letters = string.ascii_letters
    return ''.join(random.sample(letters, stringLength))

def generate(data):
    # Randomly create start_index string of length 5.
    elem = randomString(5)

    # Sample the starting and ending point
    start_index = random.randint(1, 3)
    end_index = random.randint(start_index + 1, len(elem) - 1)

    # Compute the output. 
    output = elem[start_index : end_index]

    # Store the parameters 
    data["correct_answers"]['start_index'] = start_index
    data["correct_answers"]['end_index'] = end_index
    data['params']['elem'] = elem
    data['params']['output'] = str(output)
