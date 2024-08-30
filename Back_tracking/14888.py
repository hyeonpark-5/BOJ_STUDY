# 연산자 끼워넣기
# 중복 불가
# 시간 초과
import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline
# 연산자 계산
def calculate(idx, x, y):
    if idx == 0:
        return x + y
    if idx == 1:
        return x - y
    if idx == 2:
        return x * y
    if idx == 3:
        return int(x/y)
    
def dfs(x):
    global minn, maxx
    first = a[0]
    summ = 0
    if x == m:
        for i in range(1, n):
            summ = calculate(res[i - 1], first, a[i])
            first = summ

        if summ < minn:
            minn = summ
        if summ > maxx:
            maxx = summ
       
    for i in range(m):
        if check[i] == 0:
            check[i] = 1
            res[x] = cal[i]
            dfs(x + 1)
            check[i] = 0
            
n = int(input())
m = n - 1
a = list(map(int, input().split()))
arr = list(map(int, input().split()))

cal = []
minn = 1e9
maxx = -1e9

for i in range(4):
    if arr[i] != 0:
        for j in range(arr[i]):
            cal.append(i)

res = [0] * m
check = [0] * m
dfs(0)

print(maxx)
print(minn)