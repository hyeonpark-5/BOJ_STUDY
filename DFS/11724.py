# 연결 요소의 개수
import sys
sys.setrecursionlimit(10 ** 6)
def dfs(x):
    visited[x] = 1
    for i in range(n + 1):
        if visited[i] == 0 and board[x][i]:
            visited[i] = 1
            dfs(i)
    
n, m = map(int, input().split())
board = [[0] * (n + 1) for _ in range(n + 1)]
visited = [0] * (n + 1)
cnt = 0

for _ in range(m):
    x, y = map(int, input().split())
    board[x][y] = 1
    board[y][x] = 1

for j in range(1, n + 1):
    if visited[j] == 0:
        cnt += 1
        dfs(j)

print(cnt)