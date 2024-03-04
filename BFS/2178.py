from collections import deque
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

n, m = map(int, input().split())
board = [list(map(int, input())) for _ in range(n)]
dis = [[0] * m for _ in range(n)]
q = deque()
q.append((0, 0))
# board[0][0] = 0

while q:
    tmp = q.popleft()
    for i in range(4):
        x = tmp[0] + dx[i]
        y = tmp[1] + dy[i]
        if 0 <= x < m and 0 <= y < n and board[x][y] == 1:
            board[x][y] = 0
            dis[x][y] = dis[tmp[0]][tmp[1]] + 1   
            q.append((x, y))


# while q:
#     tmp = q.popleft()

#     for i in range(4):
#         x = tmp[0] + dx[i]
#         y = tmp[1] + dy[i]
#         if 0 <= y < n  and 0 <= x < m and board[x][y] == 1:
#             # board[x][y] = 0
#             ch[x][y] = board[tmp[0]][tmp[1]] + 1
#             q.append((x, y))
    

print(dis[n - 1][m - 1])
    