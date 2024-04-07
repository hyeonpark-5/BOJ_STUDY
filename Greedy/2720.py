t = int(input())
coin = [25, 10, 5, 1]
for _ in range(t):
    give = []
    pay = int(input())
    for i in coin:
        give.append(pay // i)
        pay %= i

    print(*give)