def dfs(x, s):
    if x == m:
        for s in res:
            print(s, end = ' ')
        print()
    else:
        for i in range(s, n + 1):
            res[x] = i
            dfs(x + 1, i)

n, m = map(int, input().split())
res = [0] * m
dfs(0, 1)