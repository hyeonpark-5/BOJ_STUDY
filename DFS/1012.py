#유기농 양배추
import sys
sys.setrecursionlimit(10**6)
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def dfs(x, y):
    board[x][y] = 0

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == 1:
            board[nx][ny] = 0
            dfs(nx, ny)

t = int(input())

for _ in range(t):
    m, n, k = map(int, input().split())
    board = [[0] * (m + 1) for _ in range(n + 1)]
    cnt = 0
    for _ in range(k):
        y, x = map(int, input().split())
        board[x][y] = 1

    for i in range(n):
        for j in range(m):
            if board[i][j] == 1:
                cnt += 1
                dfs(i, j)

    print(cnt)