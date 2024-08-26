import sys
input = sys.stdin.readline
def dfs(x, s):
    if x == m:
        for i in range(m):
            print(res[i], end = ' ')
        print()
        return

    check = 0
    for i in range(n):
        if check != arr[i]:
            res[x] = arr[i]
            check = arr[i]
            dfs(x + 1, s + 1)

n, m = map(int, input().split())
arr = list(map(int, input().split()))
res = [0] * m
arr.sort()
dfs(0, 0)