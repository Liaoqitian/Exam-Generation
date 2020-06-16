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

    # Compute the output. 
    output = elem[start_index : end_index]

    # Store the parameters 
    data["correct_answers"]['start_index'] = start_index
    data["correct_answers"]['end_index'] = end_index
    data['params']['elem'] = elem
    data['params']['output'] = str(output)
