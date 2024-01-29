def dfs(x):
    if x == m:
        for s in res:
            print(s, end = ' ')
        print()
    else:
        for i in range(n):
            if ch[i] == 0:
                ch[i] = 1
                res[x] = a[i]
                dfs(x + 1)
                ch[i] = 0

n, m = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
res = [0] * m
ch = [0] * (n + 1)
dfs(0)