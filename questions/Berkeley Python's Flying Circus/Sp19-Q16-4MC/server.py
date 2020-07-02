import prairielearn as pl
import random, copy, math

def generate(data):
    # Sample an integer to place in A, and another integer to add to A. 
    number_one = random.randint(1, 9)
    raw_number_two = random.randint(1, 9)
    A = [number_one]

    # Randomly determine if number_two has a bracket. 
    booleans = [True, False]
    has_bracket = booleans[random.randint(0, 1)]
    number_two = raw_number_two
    if has_bracket: 
        number_two = [raw_number_two]
    
    # Compute the corresponding solution 
    A.append(number_two)
    solution = str(A)

    # Create wrong choices 

    if has_bracket: 
        data['params']['i0'] = "None of these"
        data['params']['i1'] = str([number_one, raw_number_two])
        data['params']['i2'] = str([number_one])
        data['params']['i3'] = str([int(str(number_one) + str(raw_number_two))])
        data['params']['i4'] = "Error"
    else: 
        data['params']['i0'] = "None of these"
        data['params']['i1'] = str([number_one, [raw_number_two]])
        data['params']['i2'] = str([number_one])
        data['params']['i3'] = str([int(str(number_one) + str(raw_number_two))])
        data['params']['i4'] = "Error"

    # Store the parameters
    data['params']['number_one'] = number_one 
    data['params']['number_two'] = str(number_two)
    data['params']['solution'] = solution 