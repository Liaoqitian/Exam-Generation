import prairielearn as pl
import random, copy, math

def generate(data):

    # Randomize the count 
    count = random.randint(5, 9)
    old_list = random.sample(range(1, 9), 2)
    new_list = [old_list for x in range(count)]
    solution = "[input_list for i in range(" + str(count) + ")]"

    # Store the variables 
    data['params']['count'] = count 
    data['params']['old_list'] = str(old_list)
    data['params']['new_list'] = str(new_list)
    data['correct_answers']['solution'] = solution