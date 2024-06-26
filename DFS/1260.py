import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

def dfs(v):
    visited[v] = 1
    print(v, end=' ')
    for i in range(1, n + 1):
        if board[v][i] and not visited[i]:
            dfs(i)

n, m ,v = map(int, input().split())
board = [[0] * (n + 1) for _ in range(n + 1)]
visited = [0] * (n + 1)
check = [0] * (n + 1)

for _ in range(m):
    x, y = map(int, input().split())
    board[x][y] = 1
    board[y][x] = 1

dfs(v)
print()
q = deque()
q.append(v)
check[v] = 1

while q:
    now = q.popleft()
    print(now, end = ' ')
    for i in range(1, n + 1):
        if board[now][i] and check[i] == 0:
            check[i] = 1
            q.append(i)
