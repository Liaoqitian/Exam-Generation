import random 

def generate(data):
    adjectives = ["big", "small", "pretty", "ugly", "red", "blue", "tall", "short"]
    nowns = ["house", "car", "tree", "table", "chair", "fork", "bird", "window"]
    key_one = adjectives[random.randint(0, 7)]
    key_two = nowns[random.randint(0, 7)]
    count_one = random.randint(0, 9)
    count_two = random.randint(0, 9)
    d = {}
    d[key_one] = count_one
    d[key_two] = count_two
    key_solution = d.keys()
    value_solution = d.values()

    data["params"]["d"] = str(d)
    data["correct_answers"]["key_solution"] = str(key_solution)
    data["correct_answers"]["value_solution"] = str(value_solution)

def grade(data): 
    if data["partial_scores"]["key_solution"]["score"] != 1: 
        if data["submitted_answers"]["key_solution"] == data['correct_answers']['key_solution'].replace("'",'"'):
            data["partial_scores"]["key_solution"]["score"] = 1
            data["score"] += 0.5

    