import random, copy, math
import numpy as np

def most_common(sequence): 
    counts = {}
    for elem in sequence: 
        if elem in counts:
            counts[elem] += 1
        else:
            counts[elem] = 1
    max_val = max(counts.values())
    return [elem for elem in counts if counts[elem] == max_val]

def least_common(sequence): 
    counts = {}
    for elem in sequence: 
        if elem in counts:
            counts[elem] += 1
        else:
            counts[elem] = 1
    min_val = min(counts.values())
    return [elem for elem in counts if counts[elem] == min_val]

def generate(data):
    # The question has two variants. 0: most common; 1: least common 
    variant = random.randint(0, 1)
    if variant == 0: 
        data["params"]["keyword"] = "most"
        data["params"]["function"] = "most_common"
        data["params"]["example_one"] = str(most_common([1, 2, 3, 3, 4, 4, 6, 4, 4, 5, 5, 5, 5]))
        data["params"]["example_two"] = str(most_common("uc berkeley also cal"))

    elif variant == 1:
        data["params"]["keyword"] = "least"
        data["params"]["function"] = "least_common"
        data["params"]["example_one"] = str(least_common([1, 2, 3, 3, 4, 4, 6, 4, 4, 5, 5, 5, 5]))
        data["params"]["example_two"] = str(least_common("uc berkeley also cal"))

    data['params']['names_for_user'] = []
    data['params']['names_from_user'] = [
        {'name':'most_common','description':'Returns a dictionary of most common elements','type':'python function'}, 
        {'name':'least_common','description':'Returns a dicionary of least common elements','type':'python function'}, 
        ]