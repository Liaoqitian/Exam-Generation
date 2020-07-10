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

def plus4(x):
    return x + 4

def plus5(x): 
    return x + 5

def times2(x):
    return x * 2

def times3(x):
    return x * 3

def generate(data):
    # The resulting function call would look like: reduce(compose, [function_one, str, function_two, function_three, function_one])
    # function_one and function_two are always paired. The two possible pairs are [double, times3] and [triple, times2]
    # function_three is a "plus" function
    function_list = [[double, times3], [triple, times2], plus1, plus4, plus5]

    # Randomizes the pair
    multiplication_functions = function_list[random.randint(0, 1)]

    # Determine which one is function_one and the other one would be function_two
    random_index = random.randint(0 ,1)
    function_one = multiplication_functions[random_index]
    function_two = multiplication_functions[1 - random_index] 

    # Randomizes the "plus" function
    function_three = function_list[random.randint(2, 4)]

    # Randomize the correct solution and compute the returned value 
    solution = random.randint(10, 20)
    returned_value = reduce(compose, [function_one, str, function_two, function_three, function_one])(solution)

    # Store the corresponding texts 
    if function_one == double: 
        data['params']['text_one'] = "def double(x): return x + x"
        data['params']['function_one'] = "double"
    elif function_one == triple: 
        data['params']['text_one'] = "def triple(x): return x + x + x"
        data['params']['function_one'] = "triple"
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
    elif function_two == times2:
        data['params']['text_two'] = "def times2(x): return x * 2"
        data['params']['function_two'] = "times2"
    else: 
        data['params']['text_two'] = "def times3(x): return x * 3"
        data['params']['function_two'] = "times3"

    if function_three == plus1:
        data['params']['text_three'] = "def plus1(x): return x + 1" 
        data['params']['function_three'] = "plus1"
    elif function_three == plus4:
        data['params']['text_three'] = "def plus4(x): return x + 4"
        data['params']['function_three'] = "plus4"
    else: 
        data['params']['text_three'] = "def plus5(x): return x + 5"
        data['params']['function_three'] = "plus5"
    
    data['correct_answers']['solution'] = solution
    data['params']['returned_value'] = returned_value

