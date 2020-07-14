import random, copy, math
import numpy as np

def generate(data):

    # Randomize the percentage of program which is serial. Store the information in params. 
    p = [5, 10, 20, 25, 50, 100] 
    idx = random.choice(range(6))
    percentage = p[idx]
    data['params']['percentage'] = percentage

    # Compute the corresponding solutions for each of the possible percentages. Determine the correct ones. Store the information in params. 
    solutions = [100 / i for i in p]
    solution = solutions[idx]
    data['params']['solution'] = solution
    # Store the incorrect solutions in params. "i" is short-hand for incorrect. 
    copy = []
    for i in range(6): 
        copy.append(solutions[i])
    copy.remove(solution)
    i0 = copy[0]
    i1 = copy[1]
    i2 = copy[2]
    i3 = copy[3]
    i4 = copy[4]
    data['params']['i0'] = i0
    data['params']['i1'] = i1
    data['params']['i2'] = i2
    data['params']['i3'] = i3
    data['params']['i4'] = i4