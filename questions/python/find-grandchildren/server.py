import prairielearn as pl
import pandas as pd
import random

def generate(data):
    # Three Variants: 
    # 0. Find Grandchildren 
    # 1. same_key 
    # 2. same_value
    variant = random.randint(0, 2) 
    data["params"]["text_one"] = "Write a function"
    data["params"]["file_name"] = str(variant) + ".png"
    if variant == 0: 
        data["params"]["variable_one"] = "GP"
        data["params"]["variable_two"] = "PC"
        data["params"]["function"] = "find_GC"
        data["params"]["text_two"] = "that takes in two dictionaries ("
        data["params"]["text_three"] = 'capturing grandparents\u2192parents, and'
        data["params"]["text_four"] = ' capturing parents\u2192children)'
        data["params"]["description"] = "returns a new dictionary of all grandparents"
        data["params"]["connector"] = "\u2192"
        data["params"]["description_two"] = "children it finds. "
        data["params"]["text_five"] = """As an example, we have three grandparents: 1, 2 and 3; three parents: 10, 11 and 12; and two children: 100 and 200 with \u2192 connections 
        as shown below. Your function would return the two grandparents\u2192children: 1\u2192100 and 2\u2192100. By the way, more than 2 grandparents 
        can\u2192to the same parent; similarly for parents\u2192children (sometimes family records get corrupted, it's not your job to worry about that). """
        data["params"]["bold_one"] = ""
        data["params"]["bold_two"] = ""
        data["params"]["bold_three"] = ""
        data["params"]["bold_four"] = ""
        data["params"]["text_six"] = ""
        data["params"]["text_seven"] = ""
        
        data["params"]["function_line_one"] = "GP = {1:10, 2:10, 3:11}"
        data["params"]["function_line_two"] = "PC = {10:100, 12:200}"
        data["params"]["function_line_three"] = "find_GC(GP, PC)"
        data["params"]["function_line_four"] = "{1:100, 2:100}"

    elif variant == 1:
        data["params"]["variable_one"] = "D1"
        data["params"]["variable_two"] = "D2"
        data["params"]["function"] = "same_keys"
        data["params"]["text_two"] = "that takes in two dictionaries (" 
        data["params"]["text_three"] = "and"
        data["params"]["text_four"] = ") and"
        data["params"]["description"] = "returns a new dictionary whose keys are all the keys that are common and whose values are a tuple of the two original values, in any order."
        data["params"]["description_two"] = ""
        data["params"]["text_five"] = """As an example, with """
        data["params"]["bold_three"] = "D1"
        data["params"]["text_six"] = "and"
        data["params"]["bold_four"] = "D2"
        data["params"]["text_seven"] = """shown below, 1 is a shared key, so the function would return a
            dictionary with the shared key 1 and a tuple of the different values (10, 20). If there were more keys that
            were the same between the two dictionaries, the returned dictionary would have more of these key tuples as well.""" 
        data["params"]["bold_one"] = ""
        data["params"]["bold_two"] = ""
        data["params"]["connector"] = ""

        data["params"]["function_line_one"] = "D1 = {1:10, 2:10, 3:11}"
        data["params"]["function_line_two"] = "D2 = {1:20, 4:30}"
        data["params"]["function_line_three"] = "same_keys(D1, D2)"
        data["params"]["function_line_four"] = "{1: (10, 20)}"

    else:
        data["params"]["variable_one"] = "D1"
        data["params"]["variable_two"] = "D2"
        data["params"]["function"] = "same_values"
        data["params"]["text_two"] = "that takes in two dictionaries ("
        data["params"]["text_three"] = "and"
        data["params"]["text_four"] = ") and"
        data["params"]["description"] = """returns a new dictionary whose keys are all the tuples (in any order) of the keys from"""
        data["params"]["bold_one"] = " D1"
        data["params"]["connector"] = " and "
        data["params"]["bold_two"] = "D2 "
        data["params"]["description_two"] = """that have a common value and whose value is that common value."""
        data["params"]["text_five"] = "As an example, with" 
        data["params"]["bold_three"] = "D1"
        data["params"]["text_six"] = "and"
        data["params"]["bold_four"] = "D2"
        data["params"]["text_seven"] = "shown below, 10 and 11 are shared values, so the function would return a dictionary with the keys and values shown below."
        
        data["params"]["function_line_one"] = "D1 = {1:10, 2:10, 3:11}"
        data["params"]["function_line_two"] = "D2 = {1:20, 4:11, 5:10}"
        data["params"]["function_line_three"] = "same_values(D1, D2)"
        data["params"]["function_line_four"] = "{(1, 5): 10, (2, 5): 10, (3, 4): 11}"

    data['params']['names_for_user'] = []
    data['params']['names_from_user'] = [
        {'name':'find_GC','description':'Returns a dictionary of grandparents','type': 'python function'}, 
        {'name':'same_keys','description':'Returns a list of tuples','type':'python function'}, 
        {'name':'same_values','description':'Returns a list of tuples','type':'python function'}, 
        ]