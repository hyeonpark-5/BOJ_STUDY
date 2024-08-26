import sys
input = sys.stdin.readline
a = ['a', 'e', 'i', 'o', 'u']

def dfs(x, s):
    if x == L:
        cnt = 0
        for i in range(5):
            if a[i] in res:
                cnt += 1
        if cnt == 0 or (L - cnt) < 2:
            return
        for i in range(L):
            print(res[i], end = '')
        print()
        return
    for i in range(s, c):
        if ch[i] == 0:
            res[x] = arr[i]
            ch[i] = 1
            dfs(x + 1, i)
            ch[i] = 0
    
L, c = map(int, input().split())
arr = list(input().split())
arr.sort()
res = [0] * L
ch = [0] * c
dfs(0, 0)