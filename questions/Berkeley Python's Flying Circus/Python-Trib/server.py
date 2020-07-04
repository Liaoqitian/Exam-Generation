import prairielearn as pl
import pandas as pd
import random
def generate(data):
    # Randomize the first three numbers: first_number, second_number, and third_number
    first_number = random.randint(-1, 1)
    second_number = random.randint(1, 3)
    third_number = random.randint(3, 5)

    # Randomize the multipliers for the first three numbers: multiplier_1, multiplier_2, multiplier_3
    multipliers = random.sample(range(1, 5), 3)
    multiplier_1 = multipliers[0]
    multiplier_2 = multipliers[1]
    multiplier_3 = multipliers[2]

    # Compute the first six numbers: first_number....sixth_number 
    fourth_number = first_number * multiplier_1 + second_number * multiplier_2 + third_number * multiplier_3
    fifth_number = second_number * multiplier_1 + third_number * multiplier_2 + fourth_number * multiplier_3
    sixth_number = third_number * multiplier_1 + fourth_number * multiplier_2 + fifth_number * multiplier_3

    #Convert multipliers into English words used in HTML file
    word_multiplier_1 = ''
    word_multiplier_2 = ''
    word_multiplier_3 = ''
    if multiplier_1 == 1: 
        word_multiplier_1 = 'one'
    elif multiplier_1 == 2:
        word_multiplier_1 = 'two'
    elif multiplier_1 ==3: 
        word_multiplier_1 = 'three'
    else: 
        word_multiplier_1 = 'four'

    if multiplier_2 == 1: 
        word_multiplier_2 = 'one'
    elif multiplier_2 == 2:
        word_multiplier_2 = 'two'
    elif multiplier_2 == 3: 
        word_multiplier_2 = 'three'
    else: 
        word_multiplier_2 = 'four'

    if multiplier_3 == 1:
        word_multiplier_3 = 'one'
    elif multiplier_3 == 2:
        word_multiplier_3 = 'two'
    elif multiplier_3 == 3: 
        word_multiplier_3 = 'three'
    else: 
        word_multiplier_3 = 'four'
    
    data['params']['first_number'] = first_number
    data['params']['second_number'] = second_number
    data['params']['third_number'] = third_number
    data['params']['fourth_number'] = fourth_number
    data['params']['fifth_number'] = fifth_number
    data['params']['sixth_number'] = sixth_number

    data['params']['multiplier_1'] = multiplier_1
    data['params']['multiplier_2'] = multiplier_2
    data['params']['multiplier_3'] = multiplier_3
    data['params']['word_multiplier_1'] = word_multiplier_1
    data['params']['word_multiplier_2'] = word_multiplier_2
    data['params']['word_multiplier_3'] = word_multiplier_3

    data['params']['names_for_user'] = []
    data['params']['names_from_user'] = [
        {'name': 'trib', 'description': 'Function to compute the $n^\\text{th}$ Tribonacci number', 'type': 'python function'}
    ]