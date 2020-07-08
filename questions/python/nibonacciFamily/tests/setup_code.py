first_number = data['params']['first_number']
second_number = data['params']['second_number']
multiplier_1 = data['params']['multiplier_1']
multiplier_2 = data['params']['multiplier_2']

ans = [0] * 22
ans[0] = first_number 
ans[1] = second_number
for i in range(2, 22):
    ans[i] = ans[i - 1] * multiplier_2 + ans[i - 2] * multiplier_1 # index is intended to count from left to right