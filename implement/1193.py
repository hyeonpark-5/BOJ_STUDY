x = int(input())

idx = 1
sum = 0
pre_sum = 0
col = 0
while sum < x:
    pre_sum = sum
    sum += idx
    idx += 1
    col += 1

row = x - pre_sum 
col -= (row - 1)
print(f'{row}/{col}')