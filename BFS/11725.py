from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
result = [0] * (n + 1)
board = [[0] for _ in range(n + 1)]
for _ in range(n - 1):
    x, y = map(int, input().split())
    board[x].append(y)
    board[y].append(x)

q = deque()
q.append(1)

while q:
    now = q.popleft()
    for i in board[now]:
        if not result[i]:
            result[i] = now
            q.append(i)

for i in range(2, n + 1):
    print(result[i])  