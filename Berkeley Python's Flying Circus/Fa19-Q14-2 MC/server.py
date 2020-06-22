import prairielearn as pl
import random, copy, math

def generate(data):

    # Sample a list of random length between 3 and 5. 
    length = random.randint(3, 6)

    # Sample random elements in (0, 1000) to fill the list. 
    A = [0] * length
    copy = [0] * length
    copy = random.sample(range(0, 1000), length)
    for i in range(length):   
        A[i] = str(copy[i])

    # Set up the question. 
    index = random.randint(1, len(A) - 2)
    adder = str(random.randint(1, 5))
    
    # Compute the correct solution.
    solution = A[index] + adder

    i0 = 'Error'
    i1 = int(A[index]) + int(adder)
    i2 = int(A[index - 1]) + int(adder)
    i3 = str(A[index - 1]) + str(adder)

    # Store the parameters.
    A = str(A).replace("'", '"')
    data['params']['A'] = A
    data['params']['index'] = index
    data['params']['adder'] = adder 
    data['params']['solution'] = solution
    data['params']['i0'] = i0 
    data['params']['i1'] = i1
    data['params']['i2'] = i2 
    data['params']['i3'] = i3 
