import random, copy, math
import numpy as np

def generate(data):
    # The possible bases are Binary, Decimal and Hex 
    Bases = ["2", "8", "x"]
    Selected_Bases = random.sample(Bases, 2)

    # The following represents the first number in decimal and its base. Store the information in params. 
    Number1 = random.randint(50, 100)
    Base1 = Selected_Bases[0]
    data['params']['Number1'] = Number1
    data['params']['Base1'] = Base1

    # Convert the first number into base form. Store the information in params. 
    Converted_Number1 = Number1
    if Base1 == "2": 
        Converted_Number1 = str(bin(Number1))
    elif Base1 == "8": 
        Converted_Number1 = str(oct(Number1))
    elif Base1 == "x":
        Converted_Number1 = str(hex(Number1))
    Converted_Number1 = Converted_Number1[2:]
    data['params']['Converted_Number1'] = Converted_Number1

    # The following represents the second number and its base. 
    Number2 = random.randint(50, 100)
    Base2 = Selected_Bases[1]
    data['params']['Number2'] = Number2
    data['params']['Base2'] = Base2

    # Convert the second number into decimal form. Store the information in params. 
    Converted_Number2 = Number2
    if Base2 == "2": 
        Converted_Number2 = str(bin(Number2))
    elif Base2 == "8":
        Converted_Number2 = str(oct(Number2))
    elif Base2 == "x":
        Converted_Number2 = str(hex(Number2))
    Converted_Number2 = Converted_Number2[2:]
    data['params']['Converted_Number2'] = Converted_Number2
    
    # Computes the solution to the problem, rounded to two significant digits. Store the information in correct_answers. 
    solution = round(Number1 / Number2, 2)
    data['correct_answers']['solution'] = solution

def decimalToBinary(num):
    # This function converts decimal number to binary # 
    if num > 1:
        curr = num % 2
        return decimalToBinary(num // 2) + str(curr)
    else: 
        return str(num)