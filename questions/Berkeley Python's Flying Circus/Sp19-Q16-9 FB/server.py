import prairielearn as pl
import random, copy, math
from functools import reduce

def double(x): 
    return x + x

def triple(x):
    return x + x + x

def plus1(x):
    return x + 1

def plus2(x):
    return x + 2

def times2(x):
    return x * 2

def times3(x):
    return x * 3

def square(x):
    return x * x

def cube(x):
    return x * x * x

def generate(data):
    # Randomize four functions 
    function_list = [double, triple, plus1, plus2, times2, times3, square, cube]
    selected_function_index = [random.randint(0, 1), random.randint(2, 3), random.randint(4, 5), random.randint(6, 7)]
    random_index = random.sample(range(4), 4)
    function_one = function_list[selected_function_index[random_index[0]]]
    function_two = function_list[selected_function_index[random_index[1]]]
    function_three = function_list[selected_function_index[random_index[2]]]
    function_four = function_list[selected_function_index[random_index[3]]]

    # Randomize the list in the list comprehension 
    D = {1: function_one, 2: function_two, 3: function_three, 4: function_four}
    random_list = random.sample(range(1, 5), 4)

    # Compute the corresponding solution
    solution = [D[i](i) for i in random_list]
    solution_one = solution[0]
    solution_two = solution[1]
    solution_three = solution[2]
    solution_four = solution[3]

    # Store the corresponding texts 
    if function_one == double: 
        data['params']['text_one'] = "def double(x): return x + x"
        data['params']['function_one'] = "double"
    elif function_one == triple: 
        data['params']['text_one'] = "def triple(x): return x + x + x"
        data['params']['function_one'] = "triple"
    elif function_one == plus1:
        data['params']['text_one'] = "def plus1(x): return x + 1" 
        data['params']['function_one'] = "plus1"
    elif function_one == plus2:
        data['params']['text_one'] = "def plus2(x): return x + 2"
        data['params']['function_one'] = "plus2"
    elif function_one == times2:
        data['params']['text_one'] = "def times2(x): return x * 2"
        data['params']['function_one'] = "times2"
    elif function_one == times3:
        data['params']['text_one'] = "def times3(x): return x * 3"
        data['params']['function_one'] = "times3"
    elif function_one == square:
        data['params']['text_one'] = "def square(x): return x * x"
        data['params']['function_one'] = "square"
    else: 
        data['params']['text_one'] = "def cube(x): return x * x * x"
        data['params']['function_one'] = "cube"
    
    if function_two == double: 
        data['params']['text_two'] = "def double(x): return x + x"
        data['params']['function_two'] = "double"
    elif function_two == triple: 
        data['params']['text_two'] = "def triple(x): return x + x + x"
        data['params']['function_two'] = "triple"
    elif function_two == plus1:
        data['params']['text_two'] = "def plus1(x): return x + 1" 
        data['params']['function_two'] = "plus1"
    elif function_two == plus2:
        data['params']['text_two'] = "def plus2(x): return x + 2"
        data['params']['function_two'] = "plus2"
    elif function_two == times2:
        data['params']['text_two'] = "def times2(x): return x * 2"
        data['params']['function_two'] = "times2"
    elif function_two == times3:
        data['params']['text_two'] = "def times3(x): return x * 3"
        data['params']['function_two'] = "times3"
    elif function_two == square:
        data['params']['text_two'] = "def square(x): return x * x"
        data['params']['function_two'] = "square"
    else: 
        data['params']['text_two'] = "def cube(x): return x * x * x"
        data['params']['function_two'] = "cube"
    
    if function_three == double: 
        data['params']['text_three'] = "def double(x): return x + x"
        data['params']['function_three'] = "double"
    elif function_three == triple: 
        data['params']['text_three'] = "def triple(x): return x + x + x"
        data['params']['function_three'] = "triple"
    elif function_three == plus1:
        data['params']['text_three'] = "def plus1(x): return x + 1" 
        data['params']['function_three'] = "plus1"
    elif function_three == plus2:
        data['params']['text_three'] = "def plus2(x): return x + 2"
        data['params']['function_three'] = "plus2"
    elif function_three == times2:
        data['params']['text_three'] = "def times2(x): return x * 2"
        data['params']['function_three'] = "times2"
    elif function_three == times3:
        data['params']['text_three'] = "def times3(x): return x * 3"
        data['params']['function_three'] = "times3"
    elif function_three == square:
        data['params']['text_three'] = "def square(x): return x * x"
        data['params']['function_three'] = "square"
    else: 
        data['params']['text_three'] = "def cube(x): return x * x * x"
        data['params']['function_three'] = "cube"

    if function_four == double: 
        data['params']['text_four'] = "def double(x): return x + x"
        data['params']['function_four'] = "double"
    elif function_four == triple: 
        data['params']['text_four'] = "def triple(x): return x + x + x"
        data['params']['function_four'] = "triple"
    elif function_four == plus1:
        data['params']['text_four'] = "def plus1(x): return x + 1" 
        data['params']['function_four'] = "plus1"
    elif function_four == plus2:
        data['params']['text_four'] = "def plus2(x): return x + 2"
        data['params']['function_four'] = "plus2"
    elif function_four == times2:
        data['params']['text_four'] = "def times2(x): return x * 2"
        data['params']['function_four'] = "times2"
    elif function_four == times3:
        data['params']['text_four'] = "def times3(x): return x * 3"
        data['params']['function_four'] = "times3"
    elif function_four == square:
        data['params']['text_four'] = "def square(x): return x * x"
        data['params']['function_four'] = "square"
    else: 
        data['params']['text_four'] = "def cube(x): return x * x * x"
        data['params']['function_four'] = "cube"

    data['correct_answers']['solution_one'] = solution_one
    data['correct_answers']['solution_two'] = solution_two
    data['correct_answers']['solution_three'] = solution_three
    data['correct_answers']['solution_four'] = solution_four
    data['params']['random_list'] = str(random_list)