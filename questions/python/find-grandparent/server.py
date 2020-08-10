import prairielearn as pl
import pandas as pd
import random

def generate(data):
    data['params']['names_for_user'] = []
    data['params']['names_from_user'] = [{'name':'find_GC','description':'Returns a dictionary of grandparents','type': 'python function'}]