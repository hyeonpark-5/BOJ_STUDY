def dfs(x):
    if x == m:
        for i in range(m):
            print(res[i], end =' ')
        print()
        return
    
    for i in range(n):
        res[x] = arr[i]
        dfs(x + 1)

n, m = map(int, input().split())
res = [0] * m
arr = list(map(int, input().split()))
arr.sort()
dfs(0)