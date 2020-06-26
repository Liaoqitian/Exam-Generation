import prairielearn as pl
import pandas as pd
def generate(data):
    data['params']['names_for_user'] = []
    data['params']['names_from_user'] = [
        {'name': 'trib', 'description': 'Function to compute the $n^\\text{th}$ Tribonacci number', 'type': 'python function'}
    ]