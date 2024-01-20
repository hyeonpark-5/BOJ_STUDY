def dfs(x):
    if x == n:
        for i in range(0, n):
            print(res[i], end = ' ')
        print()
    else:
        for i in range(1, n + 1):
            if ch[i] == 0:
                ch[i] = 1
                res[x] = i
                dfs(x + 1)
                ch[i] = 0



n = int(input())
res = [0] * (n + 1)
ch = [0] * (n + 1)
dfs(0)