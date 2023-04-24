dice = [0,0,0,0,0,0]

a,b,c = map(int,input().split())

dice[a - 1] += 1
dice[b - 1] += 1
dice[c - 1] += 1

max = max(dice)
idx = dice.index(max)
if max == 3:
    sum = 10000 + (idx + 1) * 1000
    print(sum)
elif max == 2:
    sum = 1000 + (idx + 1) * 100
    print(sum)
else:
    if a > b and a > c:
        print(a * 100)
    elif b > c and b > a:
        print(b * 100)
    elif c > a and c > b:
        print(c * 100)
    else:
        pass