t = int(input())
p = []
for _ in range(t):
    x, y = input().split()
    p.append((int(x), y))

p.sort(key=lambda x:x[0])

for age, name in p:
    print(f'{age} {name}')