# 영역 구하기
import sys
sys.setrecursionlimit(10**6)
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def dfs(x, y):
    global cnt
    cnt += 1
    board[x][y] = 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < m and 0 <= ny < n and board[nx][ny] == 0:
            board[nx][ny] = 0
            dfs(nx, ny)

m, n, k = map(int, input().split())
board = [[0] * n for _ in range(m) ]
res = []

for _ in range(k):
    xs, ys, xe, ye = map(int, input().split())

    for x in range(ys, ye):
        for y in range(xs, xe):
            board[x][y] = 1


for i in range(m):
    for j in range(n):
        if board[i][j] == 0:
            cnt = 0
            dfs(i, j)
            res.append(cnt)

print(len(res))
res.sort()
print(*res)