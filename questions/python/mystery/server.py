import random 
from math import sqrt 

def mystery1(L): 
    DB = {}
    for word in L:
        if word in DB:
            DB[word] = DB[word] + 1
        else:
            DB[word] = 1 
    return DB

def digit_count(N):
    DB = {}
    while N > 0:
        digit = N % 10
        if digit in DB:
            DB[digit] = DB[digit] + 1
        else:
            DB[digit] = 1
        N = N // 10 # Floor division
    return DB

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

# part(c) functions
def isEven(n): 
    return n % 2 == 0

def isOdd(n): 
    return n % 2 == 1

# part(d) functions
def add(x, y):
    return x + y

def mul(x, y):
    return x * y

# part(e) functions
def compose(f, g):
    return lambda x: f(g(x))

def oneplus(n):
    return n + 1

def twoplus(n):
    return n + 2

def threeplus(n):
    return n + 3

def fourtimes(n):
    return n * 4

def fivetimes(n):
    return n * 5

def tentimes(n):
    return n * 10


def generate(data): 
    # part(a)
    # Two different cases: either word count (0) or integer count (1)
    variant = random.randint(0, 1)
    if variant == 0: # word count 
        pass 

    count_one = random.randint(1, 3)
    count_two = random.randint(1, 3)
    count_three = random.randint(1, 3)
    d = {}
    d["BJC"] = count_one
    d["love"] = count_two 
    d["I"] = count_three 
    data["params"]["d"] = d
    data["params"]["d_str"] = str(d)
    data["correct_answers"]["solution_one"] = "this will be graded explicitly"

    # part(b)
    data["correct_answers"]["solution_two"] = ""

    # part(c)
    c_function_index = random.randint(0, 1)
    numbers = random.sample(range(10, 31), 7)
    data["params"]["numbers"] = str(numbers)
    if c_function_index == 0:
        data["params"]["odd_even_function"] = "isEven"
        data["params"]["odd_even_function_line_two"] = "return n % 2 == 0"
        solution_three = mystery2(isEven, numbers)
    elif c_function_index == 1:
        data["params"]["odd_even_function"] = "isOdd"
        data["params"]["odd_even_function_line_two"] = "return n % 2 == 1"
        solution_three = mystery2(isOdd, numbers)
    data["correct_answers"]["solution_three"] = str(solution_three)

    # part(d)
    d_function_index = random.randint(0, 1)
    if d_function_index == 0:
        data["params"]["add_mul_function"] = "add"
        data["params"]["add_mul_function_line_two"] = "return x + y"
        number_one = random.randint(0, 2)
        number_two = random.randint(number_one + 1, number_one + 3)
        number_three = random.randint(number_two + 1, number_two + 3)
        data["params"]["res"] = number_one + number_two + number_three

    elif d_function_index == 1:
        data["params"]["add_mul_function"] = "mul"
        data["params"]["add_mul_function_line_two"] = "return x * y"
        number_one = random.randint(1, 2)
        number_two = random.randint(number_one + 1, number_one + 3)
        number_three = random.randint(number_two + 1, number_two + 3)
        data["params"]["res"] = number_one * number_two * number_three
    data["correct_answers"]["solution_four"] = number_one
    data["correct_answers"]["solution_five"] = number_two
    data["correct_answers"]["solution_six"] = number_three

    # part(e)
    plus_functions = [oneplus, twoplus, threeplus]
    mul_functions = [fourtimes, fivetimes, tentimes]
    plus_function = plus_functions[random.randint(0, 2)]
    mul_function = mul_functions[random.randint(0, 2)]

    funList = [plus_function, mul_function, sqrt]
    newFun = mystery3(compose, funList)
    square_numbers = [4, 9, 16, 25]
    square_number = square_numbers[random.randint(0, 3)]
    result = newFun(square_number)
    data["params"]["square_number"] = square_number
    data["correct_answers"]["solution_seven"] = result

    if plus_function == oneplus:
        data["params"]["plus_function"] = "oneplus"
        data["params"]["plus_function_line_two"] = "return n + 1"
    elif plus_function == twoplus: 
        data["params"]["plus_function"] = "twoplus"
        data["params"]["plus_function_line_two"] = "return n + 2"
    elif plus_function == threeplus: 
        data["params"]["plus_function"] = "threeplus"
        data["params"]["plus_function_line_two"] = "return n + 3"

    if mul_function == fourtimes: 
        data["params"]["mul_function"] = "fourtimes"
        data["params"]["mul_function_line_two"] = "return n * 4"
    elif mul_function == fivetimes: 
        data["params"]["mul_function"] = "fivetimes"
        data["params"]["mul_function_line_two"] = "return n * 5"
    elif mul_function == tentimes:
        data["params"]["mul_function"] = "tentimes"
        data["params"]["mul_function_line_two"] = "return n * 10"        

# Helper function to grade (a)
def check(user_output, d): 
    if len(user_output) != len(d):
        return False
    for key in user_output:
        if user_output[key] != d[key]: 
            return False
    return True

def grade(data):
    # part(a) grading
    user_input = data["submitted_answers"]["solution_one"]
    if isinstance(user_input, str) and user_input != "":
        user_input = eval(user_input)
    if not isinstance(user_input, list): 
        data["partial_scores"]["solution_one"]["score"] = 0
    else: 
        user_output = mystery1(user_input)
        if check(user_output, data["params"]["d"]): 
            data["partial_scores"]["solution_one"]["score"] = 1
            data["score"] += 0.2
        else:
            data["partial_scores"]["solution_one"]["score"] = 0

    # part(d) grading
    if data["partial_scores"]["solution_four"]["score"] == 1:
        data["partial_scores"]["solution_four"]["score"] = 0
        data["score"] -= 0.05
    if data["partial_scores"]["solution_five"]["score"] == 1:
        data["partial_scores"]["solution_five"]["score"] = 0
        data["score"] -= 0.05
    if data["partial_scores"]["solution_six"]["score"] == 1:
        data["partial_scores"]["solution_six"]["score"] = 0
        data["score"] -= 0.05
        
    if data["submitted_answers"]["solution_four"] != data["submitted_answers"]["solution_five"]:
        if data["submitted_answers"]["solution_five"] != data["submitted_answers"]["solution_six"]:
            if data["submitted_answers"]["solution_four"] != data["submitted_answers"]["solution_six"]: 
                if data["params"]["add_mul_function"] == "add": 
                    if data["submitted_answers"]["solution_four"] + data["submitted_answers"]["solution_five"] + data["submitted_answers"]["solution_six"] == data["params"]["res"]: 
                        if data["partial_scores"]["solution_four"]["score"] != 1:
                            data["partial_scores"]["solution_four"]["score"] = 1
                            data["score"] += 0.05
                        if data["partial_scores"]["solution_five"]["score"] != 1:
                            data["partial_scores"]["solution_five"]["score"] = 1
                            data["score"] += 0.05
                        if data["partial_scores"]["solution_six"]["score"] != 1:
                            data["partial_scores"]["solution_six"]["score"] = 1
                            data["score"] += 0.05
                elif data["params"]["add_mul_function"] == "mul":
                    if data["submitted_answers"]["solution_four"] * data["submitted_answers"]["solution_five"] * data["submitted_answers"]["solution_six"] == data["params"]["res"]: 
                        if data["partial_scores"]["solution_four"]["score"] != 1:
                            data["partial_scores"]["solution_four"]["score"] = 1
                            data["score"] += 0.05
                        if data["partial_scores"]["solution_five"]["score"] != 1:
                            data["partial_scores"]["solution_five"]["score"] = 1
                            data["score"] += 0.05
                        if data["partial_scores"]["solution_six"]["score"] != 1:
                            data["partial_scores"]["solution_six"]["score"] = 1
                            data["score"] += 0.05