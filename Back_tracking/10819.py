def dfs(x):
    global result
    if x == n:
        summ = 0
        for i in range(1, n):
            summ += abs(res[i - 1] - res[i])
        result = max(result, summ)


    for i in range(n):
        if ch[i] == 0:
            ch[i] = 1
            res[x] = a[i]
            dfs(x + 1)
            ch[i] = 0

               
n = int(input())
a = list(map(int, input().split()))
ch = [0] * n
res = [0] * n
result = -2174000000
dfs(0)
print(result)