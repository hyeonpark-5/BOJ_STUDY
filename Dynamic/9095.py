# 1,2,3 더하기

t = int(input())

for _ in range(t):
    n = int(input())
    ds = [0] * (n + 1)
    if n == 1 or n == 2:
        print(n)
        continue
    if n == 3:
        print(4)
        continue
    ds[1] = 1
    ds[2] = 2
    ds[3] = 4
    for i in range(4, n + 1):
        ds[i] = ds[i - 1] + ds[i - 2] + ds[i - 3]
    print(ds[n])