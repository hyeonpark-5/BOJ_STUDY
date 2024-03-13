#침투
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
def dfs(x, y):
    global res
    board[x][y] = 1

    if x == m:
        res = True
        return
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < m and 0 <= ny < n and board[nx][ny] == 0:
            board[nx][ny] = 1
            dfs(nx, ny)
            board[nx][ny] = 0

m, n = map(int,input().split())
board = [list(map(int, input())) for _ in range(m)]
res = False

for i in range(n):
    if board[0][i] == 0:
        dfs(1, i)

if res == True:
    print("YES")
else:
    print("NO")