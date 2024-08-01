def dfs(x):
    if x == m:
        for i in range(m):
            print(res[i], end= ' ')
        print()
        return 

    check = 0
    for i in range(n):
        if ch[i] == 0 and check != arr[i]:
            ch[i] = 1
            res[x] = arr[i]
            check = arr[i]
            dfs(x + 1)
            ch[i] = 0


n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
res = [0] * m
ch = [0] * n
dfs(0)