import random 

def generate(data):
    numbers = ["several", "many", "few", "more", "couple", "a great number of", "a small number of", "various"]
    adjectives = ["big", "small", "pretty", "ugly", "red", "blue", "tall", "short"]
    nowns = ["houses", "cars", "trees", "tables", "chairs", "forks", "birds", "windows"]

    key_one = numbers[random.randint(0, 7)]
    key_two = adjectives[random.randint(0, 7)]
    key_three = adjectives[random.randint(0, 7)]

    count_one = random.randint(0, 9)
    count_two = random.randint(0, 9)
    count_three = random.randint(0, 9)

    d = {}
    d[key_one] = count_one
    d[key_two] = count_two
    d[key_three] = count_three

    data["params"]["d"] = str(d)
    chosen_key = [key_one, key_two, key_three][random.randint(0, 2)]
    data["params"]["chosen_key"] = str(chosen_key)
    data["correct_answers"]["solution"] = str(d[chosen_key])
    