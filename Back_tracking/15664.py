# n과 m(10)
import sys
input = sys.stdin.readline
def dfs(x, idx):
    if x == m:
        for i in range(m):
            print(res[i], end= ' ')
        print()
        return
    
    check = 0
    for i in range(idx, n):
        if ch[i] == 0 and arr[i] != check:
            ch[i] = 1
            res[x] = arr[i]
            check = arr[i]
            dfs(x + 1, i + 1)
            ch[i] = 0
            
n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
res = [0] * m
ch = [0] * n
dfs(0, 0)

