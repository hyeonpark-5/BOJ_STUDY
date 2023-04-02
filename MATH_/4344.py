n = int(input())

for i in range(0, n):
    sum = 0
    count = 0
    student = list(map(int, input().split()))
    for i in range(1, len(student)):
        sum += student[i]
    
    result = sum / student[0]
    for i in range(1, len(student)):
        if student[i] > result:
            count += 1
        
    final = (count / student[0]) * 100


    print("%.3f%%"%final)

