import prairielearn as pl
import random, copy, math

def generate(data):
    # Sample an integer to place in A, and another integer to add to A. 
    number_one = random.randint(1, 9)
    raw_number_two = random.randint(1, 9)
    A = [number_one]

    # Sample the keyword from "extend" and "append"
    keywords = ['append', 'extend']
    keyword = keywords[random.randint(0, 1)]

    # Randomly determine if number_two has a bracket. 
    booleans = [True, False]
    has_bracket = booleans[random.randint(0, 1)]
    number_two = raw_number_two
    if has_bracket: 
        number_two = [raw_number_two]
    
    # Compute the corresponding solution 
    solution = ""
    if keyword == 'extend' and not has_bracket: 
        solution = 'Error'
    elif keyword == 'append':
        A.append(number_two)
        solution = str(A)
    elif keyword == 'extend':
        A.extend(number_two)
        solution = str(A)

    # Create wrong choices 
    if keyword == 'extend' and not has_bracket:
        data['params']['i0'] = str([number_one, raw_number_two])
        data['params']['i1'] = str([number_one, [raw_number_two]])
        data['params']['i2'] = str([number_one])
        data['params']['i3'] = str([int(str(number_one) + str(raw_number_two))])
    elif keyword == 'append' and has_bracket: 
        data['params']['i0'] = "Error"
        data['params']['i1'] = str([number_one, raw_number_two])
        data['params']['i2'] = str([number_one])
        data['params']['i3'] = str([int(str(number_one) + str(raw_number_two))])

    elif keyword == 'append' and not has_bracket: 
        data['params']['i0'] = "Error"
        data['params']['i1'] = str([number_one, [raw_number_two]])
        data['params']['i2'] = str([number_one])
        data['params']['i3'] = str([int(str(number_one) + str(raw_number_two))])
    else: 
        data['params']['i0'] = "Error"
        data['params']['i1'] = str([number_one, [raw_number_two]])
        data['params']['i2'] = str([number_one])
        data['params']['i3'] = str([int(str(number_one) + str(raw_number_two))])

    # Store the parameters
    data['params']['number_one'] = number_one 
    data['params']['number_two'] = str(number_two)
    data['params']['keyword'] = keyword
    data['params']['solution'] = solution 
