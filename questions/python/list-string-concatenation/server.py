import random 

def generate(data):
    list_one = random.sample(range(0, 5), random.randint(1, 2))
    list_two = random.sample(range(6, 10), random.randint(1, 2))
    list_solution = list_one + list_two
    data["params"]["list_one"] = str(list_one)
    data["params"]["list_two"] = str(list_two)
    data["correct_answers"]["list_solution"] = str(list_solution)

    adjectives = ["big", "small", "pretty", "ugly", "red", "blue", "tall", "short"]
    nowns = ["house", "car", "tree", "table", "chair", "fork", "bird", "window"]
    string_one = adjectives[random.randint(0, 7)]
    string_two = nowns[random.randint(0, 7)]
    string_solution = string_one + string_two
    data["correct_answers"]["raw_string_solution"] = string_solution
    string_solution = str([string_solution]).replace("[","").replace("]","")
    data["params"]["string_one"] = string_one
    data["params"]["string_two"] = string_two
    data["correct_answers"]["string_solution"] = string_solution.replace("'",'"')

def grade(data):
    if data["submitted_answers"]["string_solution"] == data['correct_answers']['string_solution'].replace('"',"'"):
        data["partial_scores"]["string_solution"]["score"] = 1
        data["score"] += 0.5
    elif data["submitted_answers"]["string_solution"] == data["correct_answers"]["raw_string_solution"]:
        data["partial_scores"]["string_solution"]["score"] = 1
        data["score"] += 0.5
    