import prairielearn as pl
import random, copy, math

def generate(data):

    # Sample a random starting point and a corresponding ending point of R
    start = random.randint(0, 100)
    end = random.randint(start + 10, start + 20)
    R = [x for x in range(start, end + 1)]

    # Sample a random starting point and a corresponding ending point of list to be queried.
    start_index = random.randint(2, 4)
    end_index = random.randint(start_index + 2, start_index+ 4)

    # Put the four parameters into data['params']
    data['params']['start'] = start
    data['params']['end'] = end
    data['params']['start_index'] = start_index
    data['params']['end_index'] = end_index

    # Compute the solution. 
    solution = R[start_index: end_index]
    data["correct_answers"]['solution'] = str(solution)