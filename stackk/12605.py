n = int(input())

for i in range(1, n + 1):
    stp = []
    stl = []
    stp = list(map(str, input().split()))
    while len(stp) != 0:
        a = stp.pop()
        stl.append(a)
        
    print(f'Case #{i}:', end = ' ')
    print(*stl)
 

    

