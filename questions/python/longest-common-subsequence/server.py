import prairielearn as pl
import pandas as pd
import random

def generate(data):
    data['params']['names_for_user'] = []
    data['params']['names_from_user'] = [
        {'name': 'lcs', 'description': 'Function to compute longest common subsequence', 'type': 'python function'}
    ]