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
    data['params']['solution'] = R[start_index: end_index]
    
    # Build the confounding choices. 
    data['params']['i0'] = R[start_index: end_index + 1]
    data['params']['i1'] = R[start_index: end_index - 1]

    data['params']['i2'] = R[start_index + 1: end_index + 1]
    data['params']['i3'] = R[start_index - 1: end_index - 1]

    data['params']['i4'] = R[start_index + 1: end_index]
    data['params']['i5'] = R[start_index - 1: end_index]

    data['params']['i6'] = [x for x in range(start_index, end_index)]

    data['params']['i7'] = [x for x in range(start_index, end_index + 1)]
    data['params']['i8'] = [x for x in range(start_index, end_index - 1)]

    data['params']['i9'] = [x for x in range(start_index + 1, end_index + 1)]
    data['params']['i10'] = [x for x in range(start_index - 1, end_index - 1)]

    data['params']['i11'] = [x for x in range(start_index + 1, end_index)]
    data['params']['i12'] = [x for x in range(start_index - 1, end_index)]