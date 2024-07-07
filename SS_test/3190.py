from collections import deque
import sys
input = sys.stdin.readline
# 동 남 서 북
dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]
n = int(input()) # 보드의 크기
k = int(input()) # 사과의 개수
board = [[0] * n for _ in range(n)]
change = {} # 방향 전환
for _ in range(k):
    x, y = map(int, input().split())
    board[x - 1][y - 1] = 2 # 사과의 위치

L = int(input()) # 뱀의 방향 변환 횟수
for _ in range(L):
    x, c = input().split()
    change[int(x)] = c

t = 0 # 시간
d = 0 # 방향
q = deque()
q.append((0, 0))
board[0][0] = 1

# 1: 뱀 2: 사과 3: 뱀의 꼬리
while True:
    # 1번 뱀은 몸길이를 늘려 머리를 다음칸에 위치시킨다.
    nx = q[-1][0] + dx[d]
    ny = q[-1][1] + dy[d]
    t += 1
    # 2번 만약 벅이나 자기 자신의 몸과 부딪히면 게임이 끝난다.
    if (0 <= nx < n and 0 <= ny < n) and (nx, ny) not in q:
        # 만약 이동한 칸에 사과가 있다면, 그 칸에 있던 사과가 없어지고 꼬리는 움직이지 않는다.
        # 만약 이동한 칸에 사과가 없다면, 몸길이를 줄여서 꼬리가 위치한 칸을 비워준다. 
        if board[nx][ny] != 2:
            xx, yy = q.popleft()
            board[xx][yy] = 0 # 꼬리가 있던 자리
        
        board[nx][ny] = 1
        q.append((nx, ny))      
    else:
        break

    if t in change: # 방향 변화 확인
        if change[t] == 'D': 
            d = (d + 1) % 4 # 시계
        else:
            d = (d - 1) % 4 # 반시계
        

print(t)
