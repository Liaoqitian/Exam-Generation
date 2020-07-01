import random, copy, math
import numpy as np

def generate(data):
    # The possible bases are Binary, Decimal and Hex 
    Bases = ["2", "8", "16"]
    Selected_Bases = random.sample(Bases, 2)

    # The following represents the divisor in decimal and its base. Store the information in params. 
    divisor = random.randint(10, 20)
    divisor_base = Selected_Bases[0]
    data['params']['divisor'] = divisor
    data['params']['divisor_base'] = divisor_base

    # Convert the divisor into base form. Store the information in params. 
    converted_divisor = divisor
    if divisor_base == "2": 
        converted_divisor = str(bin(divisor))
    elif divisor_base == "8": 
        converted_divisor = str(oct(divisor))
    elif divisor_base == "16":
        converted_divisor = str(hex(divisor))
    converted_divisor = converted_divisor[2:]
    data['params']['converted_divisor'] = converted_divisor

    # Randomizes the solution to the problem. Store the information in correct_answers. 
    solution = random.randint(2, 4)
    data['correct_answers']['solution'] = solution

    # Compute the dividend and randomize its base. 
    dividend = divisor * solution
    dividend_base = Selected_Bases[1]
    data['params']['dividend'] = dividend
    data['params']['dividend_base'] = dividend_base

    # Convert the dividend into base form. Store the information in params. 
    converted_dividend = dividend
    if dividend_base == "2": 
        converted_dividend = str(bin(dividend))
    elif dividend_base == "8":
        converted_dividend = str(oct(dividend))
    elif dividend_base == "16":
        converted_dividend = str(hex(dividend))
    converted_dividend = converted_dividend[2:]
    data['params']['converted_dividend'] = converted_dividend
    

def decimalToBinary(num):
    # This function converts decimal number to binary # 
    if num > 1:
        curr = num % 2
        return decimalToBinary(num // 2) + str(curr)
    else: 
        return str(num)