import random, copy, math

def generate(data):

    # Sample a random starting point and a corresponding ending point of R
    x1 = random.randint(0, 100)
    y1 = random.randint(x1 + 10, x1 + 20)
    R = [x for x in range(x1, y1 + 1)]
    # Sample a random starting point and a corresponding ending point of list to be queried.
    x2 = random.randint(2, 6)
    y2 = random.randint(x2 + 2, x2+ 4)

    # Put the four parameters into data['params']
    data['params']['x1'] = x1
    data['params']['y1'] = y1
    data['params']['x2'] = x2
    data['params']['y2'] = y2

    # Compute the solution. 
    data['params']['solution'] = R[x2: y2]
    # Build the confounding choices. 
    data['params']['i0'] = R[x2: y2 + 1]
    data['params']['i1'] = R[x2: y2 - 1]

    data['params']['i2'] = R[x2 + 1: y2 + 1]
    data['params']['i3'] = R[x2 - 1: y2 - 1]

    data['params']['i4'] = R[x2 + 1: y2]
    data['params']['i5'] = R[x2 - 1: y2]

    data['params']['i6'] = [x for x in range(x2, y2)]

    data['params']['i7'] = [x for x in range(x2, y2 + 1)]
    data['params']['i8'] = [x for x in range(x2, y2 - 1)]

    data['params']['i9'] = [x for x in range (x2 + 1, y2 + 1)]
    data['params']['i10'] = [x for x in range(x2 - 1, y2 - 1)]

    data['params']['i11'] = [x for x in range(x2 + 1, y2)]
    data['params']['i12'] = [x for x in range(x2 - 1, y2)]