#숨바꼭질
from collections import deque
n, k = map(int, input().split())

MAX = 100000
ch = [0] * (MAX + 1)
t = [0] * (MAX + 1)
ch[n] = 1
t[n] = 0

dq = deque()
dq.append(n)

while dq:
    now = dq.popleft()
    if now == k:
        break

    for next in (now - 1, now + 1, now * 2):
        if 0 <= next <= MAX:
            if ch[next] == 0:
                dq.append(next)
                ch[next] = 1
                t[next] = t[now] + 1

print(t[k])  