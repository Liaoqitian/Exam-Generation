import prairielearn as pl
import pandas as pd
import random 
def generate(data):    
    variants = ['all', 'any', 'none']
    variant_num = random.randint(0, 2)
    variant = variants[variant_num]
    text = ""
    examples = ""
    requirement = ""
    if variant == 'all': 
        text = """A palindrome_all is a string that is spelled the same way forwards and backwards. In other words, the first letter
        MUST equal the last letter, the second letter MUST equal the second to last letter ... etc. """
        function = "is_palindrome_all"
        example_title_one = "palindrome_all Examples"
        example_title_two = "Not palindrome_All Examples"
        example_one = "refer"
        example_two = "level"
        example_three = "civic"
        counter_example_one = "berkeley"
        counter_example_two = "buffer"
        counter_example_three = "california"
        example_text = "All the characters of 'refer' are the same when reversed, meaning 'refer' = 'refer'."
        counter_example_text = "Not all the characters are the same, meaning, 'berkeley' != 'yelekreb'."
        requirement = """For the purposes of this problem, all zero-letter and one-letter words are palindrome_all's."""
    elif variant == 'any': 
        text = """A palindrome_any is a string that has at least one character match when you flip it. In other words, we need the first letter equal the last letter, 
        or the second letter equal the second to last letter, ... etc. """
        function = "is_palindrome_any"
        example_title_one = "palindrome_any Examples"
        example_title_two = "Not palindrome_Any Examples"
        example_one = "peek"
        example_two = "trust"
        example_three = "butter"
        counter_example_one = "peak"
        counter_example_two = "trustworthy"
        counter_example_three = "butterfly"
        example_text = "At least one character of 'peek' matches peek. 'peek' reversed is 'keep', the second and third characters match."
        counter_example_text = "None of the characters of 'peak' matches when reversed, meaning, 'peak' != 'kaep' for any character."
        requirement = """For the purposes of this problem, all zero-letter and one-letter words are NOT palindrome_any's. """
    else: 
        text = """A palindrome_none is a string that has no character match when you flip it. In other words, the first letter MUST NOT equal the last letter, 
        and the second letter MUST NOT equal the second to last letter ... etc. """ 
        function = "is_palindrome_none"
        example_title_one = "palindrome_none Examples"
        example_title_two = "Not palindrome_none Examples"
        example_one = "peak"
        example_two = "trustworthy"
        example_three = "butterfly"
        counter_example_one = "peek"
        counter_example_two = "trust"
        counter_example_three = "butter"
        example_text = "None of the characters of 'peak' matches when reversed, meaning, 'peak' != 'kaep' for any character."
        counter_example_text = "At least one character of 'peek' matches peek. 'peek' reversed is 'keep', the second and third characters match."
        requirement = """For the purposes of this problem, all zero-letter and one-letter words are NOT palindrome_none's. """
    
    data['params']['variant'] = variant 
    data['params']['variant_num'] = variant_num + 1
    data['params']['text'] = text 
    data['params']['function'] = function
    data['params']['example_title_one'] = example_title_one
    data['params']['example_title_two'] = example_title_two
    data['params']['example_one'] = example_one
    data['params']['example_two'] = example_two
    data['params']['example_three'] = example_three
    data['params']['counter_example_one'] = counter_example_one
    data['params']['counter_example_two'] = counter_example_two
    data['params']['counter_example_three'] = counter_example_three
    data['params']['example_text'] = example_text
    data['params']['counter_example_text'] = counter_example_text
    data['params']['requirement'] = requirement 
    
    data['params']['names_for_user'] = [
        {'name': 'all_but_first_of', 'description': 'Function to remove the first character of a string', 'type': 'python function'},
        {'name': 'all_but_last_of', 'description': 'Function to remove the last character of a string', 'type': 'python function'}
    ]
    data['params']['names_from_user'] = [
        {'name': 'is_palindrome_all', 'description': 'Function to determine whether a string is a palindrome_All', 'type': 'python function'},
        {'name': 'is_palindrome_any', 'description': 'Function to determine whether a string is a palindrome_Any', 'type': 'python function'},
        {'name': 'is_palindrome_none', 'description': 'Function to determine whether a string is a palindrome_None', 'type': 'python function'}
    ]