
for _ in range(3):
    a = list(map(int, input().split()))
    num = a.count(0)
    if num == 0:
        print('E')
    else:
        print(chr(64 + num))   
