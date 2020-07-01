import prairielearn as pl
import random, copy, math

def swap_elements(w):
    w[1] = w[2]
    w[2] = w[1]
    return w

def generate(data):
    # Sample "little" and "big"
    little = random.randint(10, 30)
    big = random.randint(40, 60)
    solution_swap_values = [little, big]

    # Sample a random array of five numbers.
    array = random.sample(range(1, 20), 5)
    data['params']['array'] = str(array)
    solution_swap_elements = swap_elements(array)

    # Store the parameters into data['params']
    data['params']['little'] = little
    data['params']['big'] = big
    data['correct_answers']['solution_swap_values'] = str(solution_swap_values)
    data['correct_answers']['solution_swap_elements'] = str(solution_swap_elements)


