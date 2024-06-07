# 회전하는 큐
from collections import deque

n, m = map(int, input().split())
location = list(map(int, input().split()))
q = deque([i for i in range(1, n + 1)])
answer = 0

for L in location:
    while True:
        if q[0] == L:
            q.popleft()
            break
        else:
            if q.index(L) <= len(q) // 2:
                q.rotate(-1) 
            else:
                q.rotate(1)
            answer += 1

print(answer)