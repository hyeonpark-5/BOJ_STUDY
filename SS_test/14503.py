# 로봇청소기 
import sys
from collections import deque
sys.setrecursionlimit(10 ** 6)
# 북, 동, 남, 서
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

# def dfs(x, y, d):
#     global cnt
#     cnt += 1
#     board[x][y] = 1

#     flag = 0
#     for i in range(4):
#         d = (n - 1) % 4
#         nx = x + dx[i]
#         ny = y + dy[i]
        
#         if 0 <= nx < r and 0 <= ny < c and board[nx][ny] == 0:
#             cnt += 1
#             board[nx][ny] = 1
#             flag += 1
#             dfs(nx, ny, d)

#     if flag == 0:
#         d = (n - 2) % 4
#         nx = x + dx[d]
#         ny = y + dy[d]
#         if 0 <= nx < r and 0 <= ny < c and board[nx][ny] == 0:
#             cnt += 1
#             board[nx][ny] = 1
#             dfs(nx, ny, d)
    
            


n, m = map(int, input().split())
r, c, d = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
cnt = 0
q = deque()
q.append((r, c, d))

while q:
    x, y, d = q.popleft()
    

