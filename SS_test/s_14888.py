def dfs(x, summ):
    global mx, mn
    if x == (n - 1):
        mx = max(summ, mx)
        mn = min(summ, mn)
        return
    
    if arr[0] != 0:
        arr[0] -= 1
        dfs(x + 1, summ + a[x + 1])
        arr[0] += 1
    
    if arr[1] != 0:
        arr[1] -= 1
        dfs(x + 1, summ - a[x + 1])
        arr[1] += 1

    if arr[2] != 0:
        arr[2] -= 1
        dfs(x + 1, summ * a[x + 1])
        arr[2] += 1

    if arr[3] != 0:
        arr[3] -= 1
        dfs(x + 1, int(summ/a[x + 1]))
        arr[3] += 1

n = int(input())
a = list(map(int, input().split()))
arr = list(map(int ,input().split()))
mn = 1e9
mx = -1e9
dfs(0, a[0])

print(mx)
print(mn)