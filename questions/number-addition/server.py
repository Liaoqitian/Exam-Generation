import random, copy, math

def generate(data):
    # The possible bases are Binary, Decimal and Hex 
    Bases = ["2", "10", "16"]
    Selected_Bases = random.sample(Bases, 3)

    # The following represents the first number in decimal and its base. Store the information in params. 
    Number1 = random.randint(5, 20)
    Base1 = Selected_Bases[0]
    data['params']['Number1'] = Number1
    data['params']['Base1'] = Base1

    # Convert the first number into base form. Store the information in params. 
    Converted_Number1 = Number1
    if Base1 == "2": 
        Converted_Number1 = str(bin(Number1))
        Converted_Number1 = Converted_Number1[2:]
    elif Base1 == "16":
        Converted_Number1 = str("0x{:X}".format(Number1))
        Converted_Number1 = Converted_Number1[2:]
    data['params']['Converted_Number1'] = Converted_Number1

    # The following represents the second number and its base. 
    Number2 = random.randint(5, 20)
    Base2 = Selected_Bases[1]
    data['params']['Number2'] = Number2
    data['params']['Base2'] = Base2

    # Convert the second number into decimal form. Store the information in params. 
    Converted_Number2 = Number2
    if Base2 == "2": 
        Converted_Number2 = str(bin(Number2))
        Converted_Number2 = Converted_Number2[2:]
    elif Base2 == "16":
        Converted_Number2 = str("0x{:X}".format(Number2))
        Converted_Number2 = Converted_Number2[2:]
    data['params']['Converted_Number2'] = Converted_Number2
    
    # Computes the solution to the problem, converted into its corresponding base representation. Store the information in correct_answers. 
    Base3 = Selected_Bases[2]
    data['params']['Base3'] = Base3
    unconverted_solution = Number1 + Number2
    solution = str(unconverted_solution)
    if Base3 == "2": 
        solution = str(bin(unconverted_solution))
        solution = solution[2:]
    elif Base3 == "16":
        solution = str("0x{:X}".format(unconverted_solution))
        solution = solution[2:]
    data['params']['solution'] = solution

    # Build confusing false choices based on the question and the correct solution. 

    # Randomize a total of 7 off-target choices, both on the left and right-hand side of the correct solution. 
    # "i" is short-hand for incorrect. 
    offset = random.choice(range(7))
    i_choices = []

    # The left offsets
    for i in range(offset + 1): 
        i_choices.append(unconverted_solution + 2 * (offset + 1) - 2 * i)

    # The right offsets
    for i in range(6 - offset): 
        i_choices.append(unconverted_solution - 2 - 2 * i)
    i0 = i_choices[0]
    i1 = i_choices[1]
    i2 = i_choices[2]
    i3 = i_choices[3]
    i4 = i_choices[4]
    i5 = i_choices[5]
    i6 = i_choices[6]
    if Base3 == "2": 
        i0 = str(bin(i0))[2:]
        i1 = str(bin(i1))[2:]
        i2 = str(bin(i2))[2:]
        i3 = str(bin(i3))[2:]
        i4 = str(bin(i4))[2:]
        i5 = str(bin(i5))[2:]
        i6 = str(bin(i6))[2:]
    elif Base3 == "16":
        i0 = str("0x{:X}".format(i0))[2:]
        i1 = str("0x{:X}".format(i1))[2:]
        i2 = str("0x{:X}".format(i2))[2:]
        i3 = str("0x{:X}".format(i3))[2:]
        i4 = str("0x{:X}".format(i4))[2:]
        i5 = str("0x{:X}".format(i5))[2:]
        i6 = str("0x{:X}".format(i6))[2:]

    # # Create two dummy choices with wrong base 
    # i9 = solution
    # i10 = solution

    # Store all the variables in params
    data['params']["i0"] = i0
    data['params']["i1"] = i1
    data['params']["i2"] = i2
    data['params']["i3"] = i3
    data['params']["i4"] = i4
    data['params']["i5"] = i5
    data['params']["i6"] = i6
    