import prairielearn as pl
import random, copy, math

def generate(data): 
    # operations map: 0 - add, 1 - minus, 2 - multiply
    operation_key = random.randint(0, 2)
    operator_number = random.randint(2, 3)
    range_number = random.randint(7, 10)
    modulo_number = random.randint(2, 4)
    remainder_number = random.randint(0, modulo_number - 1)
    if operation_key == 0: 
        operation = "+"
        outcome = [x + operator_number for x in range(range_number) if x % modulo_number != remainder_number]
    elif operation_key == 1: 
        operation = "-"
        outcome = [x - operator_number for x in range(range_number) if x % modulo_number != remainder_number]
    elif operation_key == 2:
        operation = "*"
        outcome = [x * operator_number for x in range(range_number) if x % modulo_number != remainder_number]

    data["params"]["operation_key"] = operation_key
    # data["params"]["operator_number"] = operator_number 
    data["params"]["range_number"] = range_number
    # data["params"]["modulo_number"] = modulo_number
    data["params"]["remainder_number"] = remainder_number
    # data["params"]["operation"] = operation

    data["params"]["outcome"] = str(outcome)
    data["correct_answers"]["solution_one"] = operation
    data["correct_answers"]["solution_two"] = str(operator_number)
    data["correct_answers"]["solution_three"] = str(modulo_number)