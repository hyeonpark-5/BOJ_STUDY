def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x % y)

n = int(input())
for _ in range(n):
    sum = 0
    num = list(map(int, input().split()))
    for i in range(1, len(num)):
        x = num[i]
        for j in range(i + 1, len(num)):
            y = num[j]
            sum += gcd(x, y)
                   
    print(sum)