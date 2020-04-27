import random, copy, math

def generate(data):

    # Sample one random integer between -100 and 100 (inclusive) for questions a
    a = random.randint(-100, 100)

    # Sample two random integers between 5 and 10 (inclusive) for questions part b and c. 
    b = random.randint(5, 10)
    c = random.randint(5, 10)

    # Put these three integers into data['params']
    data['params']['a'] = a
    data['params']['b'] = b
    data['params']['c'] = c

    # Compute the corresponding solutions of the three parts. (stored in "first_soln", "second_soln", and "third_soln"). 
    first_soln = number_representation(a)
    second_soln = find_min(b)
    third_soln = find_max(c)
    # Put the sum into data['correct_answers']
    data['correct_answers']['first_soln'] = first_soln
    data['correct_answers']['second_soln'] = second_soln
    data['correct_answers']['third_soln'] = third_soln

def number_representation(num):
    positive = True 
    if num < 0:
        positive = False
        num = -num
    if positive: 
        binary_number = str(0) + decimalToBinary(num)
    else: 
        binary_number = str(1) + decimalToBinary(num)
    res = "0b" + binary_number
    return res

def decimalToBinary(num):
    # This function converts decimal number to binary and prints it # 
    if num > 1:
        curr = num % 2
        return decimalToBinary(num // 2) + str(curr)
    else: 
        return str(num)

def find_min(num):
    # This function finds the minimum number (in decimal) we can represent using 5 digits in sign and magnitude
    res = -math.pow(2, num - 1) + 1
    return res

def find_max(num): 
    # This function finds the maximum number (in decimal) we can represent using 5 digits in sign and magnitude
    res = math.pow(2, num - 1) - 1
    return res 