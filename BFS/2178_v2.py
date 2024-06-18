#미로 탐색
from collections import deque
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
n, m = map(int, input().split())

board = [list(map(int, input())) for _ in range(n)]
ch = [[0] * m for _ in range(n)]

q = deque()
q.append((0, 0))
board[0][0] = 1
ch[0][0] = 1
while q:
    x, y = q.popleft()
    if x == n - 1 and y == m - 1:
        break
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == 1:
            ch[nx][ny] = ch[x][y] + 1
            board[nx][ny] = 0
            q.append((nx, ny))

print(ch[n - 1][m - 1])