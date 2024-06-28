import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def dfs(w):
    global visited
    for i in board[w]:
        if not visited[i]:
            visited[i] = 1
            dfs(i) 

n, m = map(int, input().split())
board = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)
result = 0

for _ in range(m):
    x, y = map(int, input().split())
    board[x].append(y)
    board[y].append(x)

for i in range(1, n + 1):
    if visited[i] == 0:
        result += 1
        dfs(i)

print(result)