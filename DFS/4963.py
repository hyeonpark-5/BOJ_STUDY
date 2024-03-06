# 섬의 개수
import sys
sys.setrecursionlimit(100000)
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

def dfs(x, y):
    board[x][y] = 0
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < h and 0 <= ny < w and board[nx][ny] == 1:
            board[nx][ny] = 0
            dfs(nx, ny)

while True:
    w, h = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(h)]
    cnt = 0
    if w == 0 and h == 0:
        break

    for i in range(h):
        for j in range(w):
            if board[i][j] == 1:
                cnt += 1
                dfs(i, j)

    print(cnt)
