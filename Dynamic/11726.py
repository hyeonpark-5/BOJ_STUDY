n = int(input())
ds = [0] * (n + 1)
if n == 1 or n == 2 or n == 3:
    print(n)
else:
    ds[1] = 1
    ds[2] = 2
    ds[3] = 3
    for i in range(4, n + 1):
        ds[i] = ds[i - 1] + ds[i - 2]
    print(ds[n] % 10007)