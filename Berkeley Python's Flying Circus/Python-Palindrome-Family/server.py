import prairielearn as pl
import pandas as pd
import random 
def generate(data):    
    variants = ['All', 'Any', 'None']
    variant = variants[random.randint(0, 2)]
    text = ""
    examples = ""
    requirement = ""
    if variant == 'All': 
        text = """A palindrome-All is a string that is spelled the same way forwards and backwards. In other words, the first letter
        MUST equal the last letter, the second letter MUST equal the second to last letter ... etc. """
        example_title_one = "Palindrome-All Example"
        example_title_two = "Not Palindrome-All Example"
        example_one = "refer"
        example_two = "berkeley"

        example = """For example, "refer" is a palindrome-All, because it is spelled the same forward and backward. But "berkeley" is not. """
        requirement = """For the purposes of this problem, all zero-letter and one-letter words are palindrome-All's."""
    elif variant == 'Any': 
        text = """A palindrome-Any is a string that has at least one character match when you flip it. In other words, we need the first letter equal the last letter, 
        or the second letter equal the second to last letter, ... etc. """
        example_title_one = "Palindrome-Any Example"
        example_title_two = "Not Palindrome-Any Example"
        example_one = "peek"
        example_two = "peak"

        example = """For example, "peek" is a palindrome-Any, because when you flip it, it becomes "keep". 
        Both the second and third character match that of the original string. But "peak" is not. """
        requirement = """For the purposes of this problem, all zero-letter and one-letter words are palindrome-Any's. """
    else: 
        text = """A palindrome-None is a string that has no character match when you flip it. In other words, the first letter MUST NOT equal the last letter, 
        and the second letter MUST NOT equal the second to last letter ... etc. """ 
        example_title_one = "Palindrome-None Example"
        example_title_two = "Not Palindrome-None Example"
        example_one = "peak"
        example_two = "peek"

        example = """For example, "peak" is a palindrome-None, because when you flip it, it becomes "kaep". None of the characters match. But "peek" is not. """
        requirement = """For the purposes of this problem, all zero-letter and one-letter words are NOT palindrome-None's. """

    data['params']['variant'] = variant 
    data['params']['text'] = text 
    data['params']['example_title_one'] = example_title_one
    data['params']['example_title_two'] = example_title_two
    data['params']['example_one'] = example_one
    data['params']['example_two'] = example_two
    data['params']['example'] = example

    data['params']['requirement'] = requirement 

    data['params']['names_for_user'] = [
        {'name': 'all_but_first_of', 'description': 'Function to remove the first character of a string', 'type': 'python function'},
        {'name': 'all_but_last_of', 'description': 'Function to remove the last character of a string', 'type': 'python function'}
    ]
    data['params']['names_from_user'] = [
        {'name': 'checkPalindrome', 'description': 'Function to determine whether a string is a palindrome-' + variant, 'type': 'python function'}
    ]