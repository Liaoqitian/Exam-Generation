import prairielearn as pl
import pandas as pd
def generate(data):    
    data['params']['names_for_user'] = [
        {'name': 'all_but_first_of', 'description': 'Function to remove the first character of a string', 'type': 'python function'},
        {'name': 'all_but_last_of', 'description': 'Function to remove the last character of a string', 'type': 'python function'}
    ]
    data['params']['names_from_user'] = [
        {'name': 'isPalindromeNone', 'description': 'Function to determine whether a string is a palindrome-None', 'type': 'python function'}
    ]