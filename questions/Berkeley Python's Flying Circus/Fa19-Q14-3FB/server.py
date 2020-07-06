import prairielearn as pl
import random, copy, math
from functools import reduce

def compose(f, g): 
    return lambda x: f(g(x))

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

def generate(data):
    # The resulting function call would look like: reduce(compose, [multiplication_function, str, function_one, function_two, multiplication_function])
    function_list = [double, triple, plus1, plus2, times2, times3]
    multiplication_function = function_list[random.randint(0, 1)] 
    if multiplication_function == double:
        data['params']['multiplication_function'] = 'double'
    else: 
        data['params']['multiplication_function'] = 'triple'
    selected_function_index = [random.randint(0, 1), random.randint(2, 3), random.randint(4, 5)]
    random_index = random.sample(range(3), 3)
    function_one = function_list[selected_function_index[random_index[0]]]
    function_two = function_list[selected_function_index[random_index[1]]]
    function_three = function_list[selected_function_index[random_index[2]]]

    if random_index[0] == 0: 
        function_one = multiplication_function 
    elif random_index[1] == 0:
        function_two = multiplication_function
    else: 
        function_three = multiplication_function

    # Randomize the correct solution and compute the returned value 
    solution = random.randint(10, 20)
    returned_value = reduce(compose, [multiplication_function, str, function_one, function_two, function_three])(solution)

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
    else: 
        data['params']['text_one'] = "def times3(x): return x * 3"
        data['params']['function_one'] = "times3"
    
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
    else: 
        data['params']['text_two'] = "def times3(x): return x * 3"
        data['params']['function_two'] = "times3"

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
    else: 
        data['params']['text_three'] = "def times3(x): return x * 3"
        data['params']['function_three'] = "times3"
    
    data['correct_answers']['solution'] = solution
    data['params']['returned_value'] = returned_value

