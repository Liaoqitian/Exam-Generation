import random 

def mystery2(f, L): 
    if len(L) == 0:
        return []
    else:
        first_elt = L[0]
        rest_elts = L[1:]
        if f(first_elt):
            return [first_elt] + mystery2(f, rest_elts)
        else:
            return mystery2(f, rest_elts)

def mystery3(f, L):
    if (len(L) == 1):
        return L[0]
    else:
        return f(L[0], mystery3(f, L[1:]))


def isEven(n): 
    return n % 2 == 0

def isOdd(n): 
    return n % 2 == 1

def generate(data): 
    # part (a)
    count_one = random.randint(0, 2)


    # part (c)
    function_index = random.randint(0, 1)
    numbers = random.sample(range(10, 31), 7)
    if function_index == 0:
        data["params"]["odd_even_function"] = "isEven"
        data["params"]["odd_even_function_line_two"] = "return n % 2 == 0"
        solution_three = mystery2(isEven, numbers)
        data["correct_answers"]["solution_three"] = solution_three
    elif function_index == 1:
        data["params"]["odd_even_function"] = "isOdd"
        data["params"]["odd_even_function_line_two"] = "return n % 2 == 1"
        solution_three = mystery2(isOdd, numbers)
        data["correct_answers"]["solution_three"] = solution_three