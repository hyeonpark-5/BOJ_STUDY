def dfs(x, s):
    if x == m:
        for s in res:
            print(s, end = ' ')
        print()
    else:
        for i in range(s, n):
            if ch[i] == 0:
                res[x] = a[i]
                ch[i] = 1
                dfs(x + 1, i + 1)
                ch[i] = 0

n, m = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
res = [0] * m
ch = [0] * (n + 1)
dfs(0, 0)