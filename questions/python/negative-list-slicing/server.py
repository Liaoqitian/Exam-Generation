import random 

def generate(data):
    l = random.sample(range(10), 10)
    s = ""
    for i in l:
        s += str(i)
    index = random.randint(-6, -2) 
    solution = s[index:]
    data["correct_answers"]["raw_solution"] = solution
    solution = str([solution]).replace("[","").replace("]","")
    data["params"]["s"] = s
    data["params"]["index"] = index
    data["correct_answers"]["solution"] = solution.replace("'",'"')

def grade(data):
    if data["submitted_answers"]["solution"] == data['correct_answers']['solution'].replace('"',"'"):
        data["partial_scores"]["solution"]["score"] = 1
        data["score"] += 1
    elif data["submitted_answers"]["solution"] == data["correct_answers"]["raw_solution"]: 
        data["partial_scores"]["solution"]["score"] = 1
        data["score"] += 1
    