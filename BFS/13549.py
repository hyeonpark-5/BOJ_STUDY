# 숨박꼭질 3
from collections import deque

n, k = map(int, input().split())
MAX = 100000
dis = [0] * (MAX + 1)
ch = [0] * (MAX + 1)

q = deque()
q.append(n)
dis[n] = 0
ch[n] = 1

while q:
    now = q.popleft()
    if now == k:
        break

    for idx, next in enumerate((2 * now, now - 1, now + 1)):
        if 0 <= next <= MAX:
            if ch[next] == 0:
                q.append(next)
                ch[next] = 1
                if idx != 0:
                    dis[next] = dis[now] + 1
                else:
                    dis[next] = dis[now]

print(dis[k])