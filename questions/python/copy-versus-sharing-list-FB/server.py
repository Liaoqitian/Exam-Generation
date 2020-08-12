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

def grade(data):
    if data["score"] != 1:
        if data["submitted_answers"]["solution_swap_values"] != data['correct_answers']['solution_swap_values']:
            data["feedback"]["solution_swap_values"] = "A and B are local variables (input parameters), so changes to them directly do not change the called values."
        if data["submitted_answers"]["solution_swap_elements"] != data['correct_answers']['solution_swap_elements']:
            data["feedback"]["solution_swap_elements"] = """w is a local variable, so changes to it directly do not change the called values. 
            However, just as in Snap!, if w is a list, we can change the elements of w within the procedure. But this does not swap the values, it does it incorrectly. 
            First clobbering the value of the second element with the third. The second line of swap_elements does nothing, since there is already two 7s in the second
            and third location. """