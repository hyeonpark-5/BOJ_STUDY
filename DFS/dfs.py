def dfs(x, idx):
    if x == m:
        for i in res:
            print(i, end = ' ')
    
    for i in range(idx, n + 1):
        res[x] = arr[i]
        dfs(x + 1, idx + 1)


n, m = map(int, input().split())
arr = list(map(int, input().split()))
res = [0] * (n + 1)
dfs(0, 1)