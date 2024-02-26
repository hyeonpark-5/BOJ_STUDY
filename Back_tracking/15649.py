def dfs(x):
    if x == m:
        for i in range(x):
            print(res[i], end = ' ')
        print()
    else:
        for i in range(1, n + 1):
            if ch[i] == 0:
                ch[i] = 1
                res[x] = i
                dfs(x + 1)
                ch[i] = 0

n, m = map(int, input().split())
res = [0] * n
ch = [0] * (n + 1)
dfs(0)