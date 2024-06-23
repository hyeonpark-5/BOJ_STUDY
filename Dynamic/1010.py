t = int(input())

for _ in range(t):
    right, left = map(int, input().split())
    r = [i for i in range(0, right + 1)]
    L = [i for i in range(0, left + 1)]
    ds = [0] * [L + 1]
    if L == 1 or L == 2:
        print(L)
        continue
    
    ds[1] = 1
    ds[2] = 2
    for i in range(3, left + 1):
        maxx = 0
        for j in range(i - 1, -1, -1):
           print(j)