number_one = data['params']['number_one']
number_two = data['params']['number_two']
multiplier_one = data['params']['multiplier_one']
multiplier_two = data['params']['multiplier_two']

ans = [0] * 22
ans[0] = number_one 
ans[1] = number_two
for i in range(2, 22):
    ans[i] = ans[i - 1] * multiplier_two + ans[i - 2] * multiplier_one # index is intended to count from left to right