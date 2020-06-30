import prairielearn as pl
import random, copy, math

def generate(data):
    # Sample an integer to place in A, and another integer to add to A. 
    number_one = random.randint(1, 9)
    number_two = random.randint(1, 9)
    A = [number_one]

    # Sample the keyword from "extend" and "append"
    keywords = ['append', 'extend']
    keyword = keywords[random.randint(0, 1)]

    # Randomly determine if number_two has a bracket. 
    booleans = [True, False]
    has_bracket = booleans[random.randint(0, 1)]

    if has_bracket: 
        number_two = [number_two]

    # Compute the corresponding solution 
    solution = ""
    if keyword == 'extend' and not has_bracket: 
        solution = 'Error'
    elif keyword == 'append':
        A.append(number_two)
    elif keyword == 'extend':
        A.extend(number_two)
    solution = str(A)

    # Store the parameters
    data['params']['number_one'] = number_one 
    data['params']['number_two'] = str(number_two)
    data['params']['A'] = A
    data['params']['keyword'] = keyword
    data['correct_answers']['solution'] = solution 
