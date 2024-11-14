m, n = map(int, input().split())
result = []
for num in range(m, n + 1):
    if num == 1:
        continue
    check = 0
    for i in range(2, int(num **(1/2)) + 1):
        if num % i == 0:
            check += 1
            break
    
    if check == 0:
        result.append(num)

for n in result:
    print(n)