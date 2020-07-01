import prairielearn as pl
import pandas as pd
import random
def generate(data):
    # Randomize the first two numbers: first_number and second_number
    first_number = random.randint(-1, 1)
    second_number = random.randint(1, 3)

    # Randomize the multipliers for the first two numbers: multiplier_1 and multiplier_2
    multiplier_1 = random.randint(1, 4)
    multiplier_2 = random.randint(2, 4)

    # Compute the first six numbers: first_number....sixth_number 
    third_number = first_number * multiplier_1 + second_number * multiplier_2
    fourth_number = second_number * multiplier_1 + third_number * multiplier_2
    fifth_number = third_number * multiplier_1 + fourth_number * multiplier_2
    sixth_number = fourth_number * multiplier_1 + fifth_number * multiplier_2

    #Convert multipliers into English words used in HTML file
    word_multiplier_1 = ''
    word_multiplier_2 = ''
    if multiplier_1 == 1: 
        word_multiplier_1 = 'one'
    elif multiplier_1 == 2:
        word_multiplier_1 = 'two'
    elif multiplier_1 ==3: 
        word_multiplier_1 = 'three'
    else: 
        word_multiplier_1 = 'four'

    if multiplier_2 == 2:
        word_multiplier_2 = 'two'
    elif multiplier_2 == 3: 
        word_multiplier_2 = 'three'
    else: 
        word_multiplier_2 = 'four'

    #Store the variable:
    data['params']['first_number'] = first_number
    data['params']['second_number'] = second_number
    data['params']['third_number'] = third_number
    data['params']['fourth_number'] = fourth_number
    data['params']['fifth_number'] = fifth_number
    data['params']['sixth_number'] = sixth_number

    data['params']['multiplier_1'] = multiplier_1
    data['params']['multiplier_2'] = multiplier_2
    data['params']['word_multiplier_1'] = word_multiplier_1
    data['params']['word_multiplier_2'] = word_multiplier_2

    data['params']['names_for_user'] = []
    data['params']['names_from_user'] = [
        {'name': 'nib', 'description': 'Function to compute the $n^\\text{th}$ Fibonacci number', 'type': 'python function'}
    ]