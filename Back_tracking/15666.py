import sys
input = sys.stdin.readline

def dfs(x, s):
    if x == m:
        for i in range(m):
            print(res[i], end = ' ')
        print()
        return
    
    check = 0
    for i in range(s, n):
        if check != arr[i]:
            res[x] = arr[i]
            check = arr[i]
            dfs(x + 1, i)
n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
res = [0] * m
dfs(0, 0)