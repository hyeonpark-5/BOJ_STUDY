from collections import deque
import copy
import sys
input = sys.stdin.readline
# 상하좌우
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs():
    q = deque()
    new_board = copy.deepcopy(board)

    for i in range(n):
        for j in range(m):
            if new_board[i][j] == 2:
                q.append((i, j))

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and new_board[nx][ny] == 0:
                new_board[nx][ny] = 2
                q.append((nx, ny))
    
    global answer
    c = 0
    for i in range(n):
        for j in range(m):
            if new_board[i][j] == 0:
                c += 1
    
    answer = max(answer, c)

def wall(cnt):
    if cnt == 3:
        bfs()
        return 
    
    for i in range(n):
        for j in range(m):
            if board[i][j] == 0:
                board[i][j] = 1
                wall(cnt + 1)
                board[i][j] = 0

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
answer = 0
wall(0)
print(answer)