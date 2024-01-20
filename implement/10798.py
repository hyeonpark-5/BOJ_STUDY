from collections import deque
s = []

for _ in range(5):
    a = deque(list(input()))
    s.append(a)

result = ''
ch = [0] * 5
while all(ch) != True:
    for i in range(5):
        if not s[i]:
            ch[i] = 1
            continue
        else:
            result += s[i].popleft()

print(result)