import random 
import string

def generate_list():
    letters = string.ascii_lowercase
    length = random.randint(2, 3) 
    l = [0] * length 
    for index in range(length):
        result_str = ''.join(random.sample(letters, random.randint(1, 4)))
        l[index] = result_str
    return l

def generate(data):
    length = random.randint(2, 3)
    l = [0] * length
    for index in range(length):
        l[index] = generate_list()
    index_one = random.randint(0, length - 1)
    index_two = random.randint(0, len(l[index_one]))
    solution = l[index_one][index_two]
    solution = str([solution]).replace("[","").replace("]","")

    data["params"]["l"] = str(l)
    data["params"]["index_one"] = index_one
    data["params"]["index_two"] = index_two
    data["correct_answers"]["solution"] = solution.replace("'",'"')

def grade(data):
    if data["submitted_answers"]["solution"] == data['correct_answers']['solution'].replace('"',"'"):
        data["partial_scores"]["solution"]["score"] = 1
        data["score"] += 1
    
