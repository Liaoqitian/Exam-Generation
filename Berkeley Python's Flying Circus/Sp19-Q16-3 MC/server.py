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

    # Compute the solution. 
    solution = elem[start_index : end_index]

    # Build the confounding choices. 
    if end_index - start_index == 1:
        i0 = elem[start_index : end_index - 1]
        i1 = 'Error'
        i2 = elem[end_index]
        i3 = elem[start_index - 1: end_index - 1]
        i4 = 'None of these'
    else: 
        i0 = elem[start_index : end_index - 1]
        i1 = 'Error'
        i2 = elem[start_index + 1: end_index - 1]
        i3 = elem[start_index - 1: end_index - 1]
        i4 = 'None of these'

    # Store the parameters 
    data['params']['elem'] = elem
    data['params']['start_index'] = start_index
    data['params']['end_index'] = end_index
    data['params']['solution'] = solution
    
    data['params']['i0'] = pl.to_json(i0) 
    data['params']['i1'] = pl.to_json(i1) 
    data['params']['i2'] = pl.to_json(i2) 
    data['params']['i3'] = pl.to_json(i3) 
    data['params']['i4'] = pl.to_json(i4) 