import prairielearn as pl
import random, copy, math

def generate(data):
    # Sample from a list of possible strings 
    lst = ['SUGAR', 'MAINE', 'CASEY', 'SPEAR', 'PEACE', 'PRICY']
    elem = random.choice(lst)

    # Sample the starting and ending point
    a = random.randint(1, 3)
    b = random.randint(a + 1, a + 3)

    # Compute the solution. 
    # if b > len(elem):
    #     solution = "Error"
    # else: 
    solution = elem[a:b]

    # Build the confounding choices. 
    # if solution == "Error": 
    #     i0 = elem[a : b - 1]
    #     i1 = elem[a : b - 2]
    #     i2 = elem[a + 1: b - 1]
    #     i3 = elem[a - 1: b - 1]
    #     i4 = 'None of these'
    if b - a == 1:
        i0 = elem[a : b - 1]
        i1 = 'Error'
        i2 = elem[b]
        i3 = elem[a - 1: b - 1]
        i4 = 'None of these'
    else: 
        i0 = elem[a : b - 1]
        i1 = 'Error'
        i2 = elem[a + 1: b - 1]
        i3 = elem[a - 1: b - 1]
        i4 = 'None of these'

    # Store the parameters 
    data['params']['elem'] = elem
    data['params']['a'] = a
    data['params']['b'] = b
    data['params']['solution'] = solution
    data['params']['i0'] = pl.to_json(i0) 
    data['params']['i1'] = pl.to_json(i1) 
    data['params']['i2'] = pl.to_json(i2) 
    data['params']['i3'] = pl.to_json(i3) 
    data['params']['i4'] = pl.to_json(i4) 
