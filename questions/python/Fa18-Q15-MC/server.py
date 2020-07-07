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
    
    #Build wrong choices
    v_i1 = [little, little]
    v_i2 = [big, big]
    v_i3 = [big, little]
    v_i4 = "Error"
    v_i5 = "None of these"

    # Sample a random array of five numbers.
    array = random.sample(range(1, 20), 5)
    data['params']['array'] = str(array)
    
    # Build wrong choices
    e_i1 = [array[0], array[2], array[1], array[3], array[4]]
    e_i2 = [array[0], array[1], array[1], array[3], array[4]]
    e_i3 = [array[1], array[0], array[2], array[3], array[4]]
    e_i4 = "Error"
    e_i5 = "None of these"

    solution_swap_elements = swap_elements(array)

    # Store the parameters into data['params']
    data['params']['little'] = little
    data['params']['big'] = big
    data['params']['v_i1'] = str(v_i1)
    data['params']['v_i2'] = str(v_i2)
    data['params']['v_i3'] = str(v_i3)
    data['params']['v_i4'] = v_i4
    data['params']['v_i5'] = v_i5

    data['params']['e_i1'] = str(e_i1)
    data['params']['e_i2'] = str(e_i2)
    data['params']['e_i3'] = str(e_i3)
    data['params']['e_i4'] = e_i4
    data['params']['e_i5'] = e_i5

    data['params']['solution_swap_values'] = str(solution_swap_values)
    data['params']['solution_swap_elements'] = str(solution_swap_elements)

def grade(data):
    if data["score"] != 1:
        if data["submitted_answers"]["input_1"] != data['params']['solution_swap_values']:
            data["feedback"]["solution_swap_values"] = "A and B are local variables (input parameters), so changes to them directly do not change the called values."
        if data["submitted_answers"]["input_2"] != data['params']['solution_swap_elements']:
            data["feedback"]["solution_swap_elements"] = """w is a local variable, so changes to it directly do not change the called values. 
            However, just as in Snap!, if w is a list, we can change the elements of w within the procedure. But this does not swap the values, it does it incorrectly. 
            First clobbering the value of the second element with the third. The second line of swap_elements does nothing, since there is already two 7s in the second
            and third location. """