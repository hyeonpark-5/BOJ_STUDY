# 바이러스 
def dfs(v):
    global count
    visited[v] = 1
    count += 1

    for i in range(n + 1):
        if board[v][i] and not visited[i]:
            dfs(i)   

n = int(input())
m = int(input())
visited = [0] * (n + 1)
count = -1 
board = [[0] * (n + 1) for _ in range(n + 1)]

for _ in range(m):
    x, y = map(int, input().split())
    board[x][y] = 1
    board[y][x] = 1

dfs(1)
print(count)