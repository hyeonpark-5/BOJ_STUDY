def dfs(x, s):
    if x == 6:
        for i in res:
            print(i, end = ' ')
        print()
        return
    
    check = 0
    for i in range(s, arr[0] + 1):
        if check != arr[i] and d[i] == 0:
            d[i] = 1
            res[x] = arr[i]
            check = arr[i]
            dfs(x + 1, i)
            d[i] = 0

while True:
    arr = list(map(int, input().split()))
    res = [0] * 6
    d = [0] * (arr[0] + 1)
    if len(arr) == 1 and arr[0] == 0:
        break
    dfs(0, 1)
    print()