import prairielearn as pl
import random, copy, math

def generate(data): 
    # map operations map: 0 - add, 1 - minus, 2 - multiply
    map_operation_key = random.randint(0, 2)

    map_number = random.randint(2, 3)
    range_number = random.randint(7, 10)
    modulo_number = random.randint(2, 4)
    remainder_number = random.randint(0, modulo_number - 1)
    
    if map_operation_key == 0: 
        map_operation = "+"
        outcome = [x + map_number for x in range(range_number) if x % modulo_number != remainder_number]
    elif map_operation_key == 1: 
        map_operation = "-"
        outcome = [x - map_number for x in range(range_number) if x % modulo_number != remainder_number]
    elif map_operation_key == 2:
        map_operation = "*"
        outcome = [x * map_number for x in range(range_number) if x % modulo_number != remainder_number]
        
    data["params"]["operation_key"] = map_operation_key
    data["params"]["range_number"] = range_number
    data["params"]["remainder_number"] = remainder_number
    data["params"]["outcome"] = str(outcome)
    data["params"]["remainder_number"] = str(remainder_number)

    data["correct_answers"]["map_operation"] = map_operation
    data["correct_answers"]["map_number"] = str(map_number)
    data["correct_answers"]["modulo_number"] = str(modulo_number)
    
        