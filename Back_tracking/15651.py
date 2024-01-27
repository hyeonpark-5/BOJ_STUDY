def dfs(x):
    if x == m:
        for i in res:
            print(i, end = ' ')
        print()
    else:
        for i in range(1, n + 1):
            res[x] = i
            dfs(x + 1)


n, m = map(int, input().split())
res = [0] * m
dfs(0)