import prairielearn as pl
import pandas as pd
import random

def generate(data): 
    data['params']['names_for_user'] = []
    data['params']['names_from_user'] = [
        {'name': 'TAs_with_at_least_half_discussions_full', 'description': 'Function to return TAs with at least half discussions full', 'type': 'python function'}
    ]