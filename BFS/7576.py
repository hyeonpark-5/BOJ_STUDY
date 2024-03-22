#토마토
import sys
from collections import deque
sys.setrecursionlimit(10 ** 6)

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

m, n = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
ch = [[0] * m for _ in range(n)]
result = 0
flag = 0

q = deque()

for i in range(n):
    for j in range(m):
        if board[i][j] == 1:
            q.append((i, j))

while q:
    tmp = q.popleft()

    for i in range(4):
        nx = tmp[0] + dx[i]
        ny = tmp[1] + dy[i]

        if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == 0:
            board[nx][ny] = 1
            ch[nx][ny] = ch[tmp[0]][tmp[1]] + 1
            q.append((nx, ny))


for i in range(n):
    for j in range(m):
        if board[i][j] == 0:
            flag = 1

if flag == 0:
    for i in range(n):
        m = max(ch[i])
        if m > result:
            result = m
    print(result)
else:
    print(-1)

