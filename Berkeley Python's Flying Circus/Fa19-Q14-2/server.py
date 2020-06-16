import prairielearn as pl
import random, copy, math

def generate(data):

    # Sample a list of random length between 3 and 5. 
    l = random.randint(3, 6)

    # Sample random elements in (0, 1000) to fill the list. 

    A = [0] * l
    for i in range(l):
        sq = random.randint(0, 2)    
        if sq == 0:
            A[i] = random.randint(0, 1000)
        else: 
            A[i] = str(random.randint(0, 1000))

    # Set up the question. 
    i = random.randint(0, len(A) - 2)
    sa = random.randint(0, 2)
    adder = random.randint(1, 5)
    if sa == 1: 
        adder = str(adder)
    
    # Compute the correct solution.
    try:
        solution = A[i] + adder
    except TypeError:
        solution = 'Error'
    
    # Create wrong choices.
    if solution == 'Error': 
        i0 = int(A[i]) + int(adder)
        i1 = str(A[i]) + str(adder)
        i2 = int(A[i - 1]) + int(adder)
        i3 = str(A[i - 1]) + str(adder)
        i4 = int(A[i + 1]) + int(adder)
        i5 = str(A[i + 1]) + str(adder)

        # Create replicates of the previous six wrong choices, but with brackets around them. This will be handled by the html file. 
        i6 = [i0]
        i7 = [i1]
        i8 = [i2]
        i9 = [i3]
        i10 = [i4]
        i11 = [i5]

    elif isinstance(solution, str):
        i0 = int(A[i]) + int(adder)
        i1 = 'Error'
        i2 = int(A[i - 1]) + int(adder)
        i3 = str(A[i - 1]) + str(adder)
        i4 = int(A[i + 1]) + int(adder)
        i5 = str(A[i + 1]) + str(adder)

        # Create replicates of the previous six wrong choices, but with brackets around them. This will be handled by the html file. 
        i6 = [i0]
        i7 = [solution]
        i8 = [i2]
        i9 = [i3]
        i10 = [i4]
        i11 = [i6]

    else: 
        i0 = 'Error'
        i1 = str(A[i]) + str(adder)
        i2 = int(A[i - 1]) + int(adder)
        i3 = str(A[i - 1]) + str(adder)
        i4 = int(A[i + 1]) + int(adder)
        i5 = str(A[i + 1]) + str(adder)
        
        # Create replicates of the previous six wrong choices, but with brackets around them. This will be handled by the html file. 
        i6 = [solution]
        i7 = [i1]
        i8 = [i2]
        i9 = [i3]
        i10 = [i4]
        i11 = [i5]

    # Store the parameters.
    # data['params']['A'] = str(A).replace("'", '"') # Preformat as string
    A = str(A).replace("'", '"')
    test = 'A' + '[' + str(i) + "] + " 
    data['params']['test'] = test
    data['params']['A'] = pl.to_json(A)
    data['params']['i'] = i
    data['params']['adder'] = pl.to_json(adder) 
    data['params']['solution'] = pl.to_json(solution)
    data['params']['i0'] = pl.to_json(i0) 
    data['params']['i1'] = pl.to_json(i1) 
    data['params']['i2'] = pl.to_json(i2) 
    data['params']['i3'] = pl.to_json(i3) 
    data['params']['i4'] = pl.to_json(i4) 
    data['params']['i5'] = pl.to_json(i5) 
    data['params']['i6'] = pl.to_json(i6) 
    data['params']['i7'] = pl.to_json(i7) 
    data['params']['i8'] = pl.to_json(i8) 
    data['params']['i9'] = pl.to_json(i9) 
    data['params']['i10'] = pl.to_json(i10) 
    data['params']['i11'] = pl.to_json(i11) 
