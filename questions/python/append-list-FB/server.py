import prairielearn as pl
import random, copy, math

def generate(data):
    # Sample an integer to place in A, and another integer to add to A. 
    number_one = random.randint(1, 9)
    number_two = random.randint(1, 9)
    A = [number_one]

    # Randomly determine if number_two has a bracket. 
    booleans = [True, False]
    has_bracket = booleans[random.randint(0, 1)]

    if has_bracket: 
        number_two = [number_two]

    # Compute the corresponding solution 
    A.append(number_two)
    solution = str(A)

    # Store the parameters
    data['params']['number_one'] = number_one 
    data['params']['number_two'] = str(number_two)
    data['params']['A'] = A
    data['correct_answers']['solution'] = solution 
