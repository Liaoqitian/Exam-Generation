import prairielearn as pl
import pandas as pd
def generate(data):
    d = {'0': [0], '1': [1], '2': [1], '3': [2], '4': [3], '5': [5]}
    df = pd.DataFrame(data = d)
    data['params']['df'] = pl.to_json(df)

    data['params']['names_for_user'] = []
    data['params']['names_from_user'] = [
        {'name': 'fib', 'description': 'Function to compute the $n^\\text{th}$ Fibonacci number', 'type': 'python function'}
    ]