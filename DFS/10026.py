#적록색약
import sys
sys.setrecursionlimit(10 ** 6)
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def dfs(x, y, w):
    check[x][y] = 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == w and check[nx][ny] == 0:
            check[nx][ny] = 1
            dfs(nx, ny, w) 
            
n = int(input())
board = [list(input()) for _ in range(n)]
check = [[0] * n for _ in range(n)]

cnt = 0
res = 0

for i in range(n):
    for j in range(n):
        if check[i][j] == 0:
            cnt += 1
            dfs(i, j, board[i][j])

check = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(n):
    for j in range(n):
        if board[i][j] == 'G':
            board[i][j] = 'R'

for i in range(n):
    for j in range(n):
        if check[i][j] == 0:
            res += 1
            dfs(i, j, board[i][j])

print(cnt, res)