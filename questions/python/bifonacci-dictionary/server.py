import prairielearn as pl
import pandas as pd
import random
def generate(data):
    # Randomize the first three numbers: number_one, number_two, and number_three
    number_one = random.randint(-1, 1)
    number_two = random.randint(1, 3)
    number_three = random.randint(3, 5)

    # Randomize the multipliers for the first three numbers: multiplier_one, multiplier_two, multiplier_three
    multipliers = random.sample(range(1, 5), 3)
    multiplier_one = multipliers[0]
    multiplier_two = multipliers[1]
    multiplier_three = multipliers[2]

    # Compute the first six numbers: number_one....number_six 
    number_four = number_one * multiplier_one + number_two * multiplier_two + number_three * multiplier_three
    number_five = number_two * multiplier_one + number_three * multiplier_two + number_four * multiplier_three
    number_six = number_three * multiplier_one + number_four * multiplier_two + number_five * multiplier_three

    #Convert multipliers into English words used in HTML file
    word_multiplier_one = ''
    word_multiplier_two = ''
    word_multiplier_three = ''
    if multiplier_one == 1: 
        word_multiplier_one = 'one'
    elif multiplier_one == 2:
        word_multiplier_one = 'two'
    elif multiplier_one ==3: 
        word_multiplier_one = 'three'
    else: 
        word_multiplier_one = 'four'

    if multiplier_two == 1: 
        word_multiplier_two = 'one'
    elif multiplier_two == 2:
        word_multiplier_two = 'two'
    elif multiplier_two == 3: 
        word_multiplier_two = 'three'
    else: 
        word_multiplier_two = 'four'

    if multiplier_three == 1:
        word_multiplier_three = 'one'
    elif multiplier_three == 2:
        word_multiplier_three = 'two'
    elif multiplier_three == 3: 
        word_multiplier_three = 'three'
    else: 
        word_multiplier_three = 'four'
    
    data['params']['number_one'] = number_one
    data['params']['number_two'] = number_two
    data['params']['number_three'] = number_three
    data['params']['number_four'] = number_four
    data['params']['number_five'] = number_five
    data['params']['number_six'] = number_six

    data['params']['multiplier_one'] = multiplier_one
    data['params']['multiplier_two'] = multiplier_two
    data['params']['multiplier_three'] = multiplier_three
    data['params']['word_multiplier_one'] = word_multiplier_one
    data['params']['word_multiplier_two'] = word_multiplier_two
    data['params']['word_multiplier_three'] = word_multiplier_three

    data['params']['names_for_user'] = []
    data['params']['names_from_user'] = [
        {'name': 'bif_dict', 'description': 'Function to return a dictionary of the first N Bifonacci number', 'type': 'python function'}
    ]