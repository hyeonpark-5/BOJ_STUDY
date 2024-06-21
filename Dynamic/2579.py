n = int(input())
stair = [0]
ds = [0] * (n + 1)
for _ in range(n):
    stair.append(int(input()))

if n == 1:
    print(stair[1])
elif n == 2:
    print(stair[1] + stair[2])
else:
    ds[1] = stair[1]
    ds[2] = stair[1] + stair[2]
    for i in range(3, n + 1):
        ds[i] = max(ds[i - 2] + stair[i], ds[i - 3] + stair[i - 1] + stair[i])
    print(ds[-1])