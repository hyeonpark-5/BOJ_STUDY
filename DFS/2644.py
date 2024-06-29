import sys
sys.setrecursionlimit(10 ** 6)
def dfs(v, count):
    global answer
    check[v] = 1
    if v == b:
        answer = count
        return 
    for i in range(1, n + 1):
        if not check[i] and board[v][i]:
            dfs(i, count + 1)


n = int(input())
a, b = map(int, input().split())
m = int(input())
board = [[0] * (n + 1) for _ in range(n + 1)]
check = [0] * (n + 1)
answer = -1

for _ in range(m):
    x, y = map(int, input().split())
    board[x][y] = 1
    board[y][x] = 1

dfs(a, 0)
print(answer)