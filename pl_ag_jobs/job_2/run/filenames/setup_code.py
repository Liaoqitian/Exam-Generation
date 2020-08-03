number_one = data['params']['number_one']
number_two = data['params']['number_two']
number_three = data['params']['number_three']
multiplier_one = data['params']['multiplier_one']
multiplier_two = data['params']['multiplier_two']
multiplier_three = data['params']['multiplier_three']

ans = [0] * 22
ans[0] = number_one 
ans[1] = number_two
ans[2] = number_three
for i in range(3, 22):
    ans[i] = ans[i - 1] * multiplier_three + ans[i - 2] * multiplier_two + ans[i - 3] * multiplier_one # index is intended to count from left to right