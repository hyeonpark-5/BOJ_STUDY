from collections import deque
word = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
s = deque(input())
check = ''
result = 0
while s:
    a = s.popleft()
    check += a
    if len(check) > 1 and check in word:
        result += 1
        check = ''
    elif len(check) > 1 and check not in word:
        if check == 'dz':
            continue
        if len(check) > 2:
            result += 1
        result += 1
        check = a
    else:
        continue

if check != '':
    result += len(check)
print(result)

