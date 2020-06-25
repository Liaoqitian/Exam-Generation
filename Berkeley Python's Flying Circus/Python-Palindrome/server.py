import prairielearn as pl
import pandas as pd
def generate(data):    
    data['params']['names_for_user'] = []
    data['params']['names_from_user'] = [
        {'name': 'isPalindrome', 'description': 'Function to determine whether a string is a palindrome', 'type': 'python function'}
    ]