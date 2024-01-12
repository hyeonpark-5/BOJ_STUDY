from collections import deque
n = int(input())
num = deque([i for i in range(n, 0, -1)])

if len(num) == 1:
    print(num[0])
else:
    while len(num) > 1:
        num.pop()
        num.appendleft(num[-1])
        num.pop()

    print(num[0])