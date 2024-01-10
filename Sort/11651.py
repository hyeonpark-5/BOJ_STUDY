t = int(input())
p = []
for _ in range(t):
    x, y = map(int, input().split())
    p.append((x, y))

p.sort(key = lambda x:(x[1], x[0]))

for x, y in p:
    print(x, y)