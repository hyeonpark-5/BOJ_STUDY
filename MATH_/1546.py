number = int(input())
score = list(map(int, input().split()))
M = max(score)
sum = 0
for i in range(0,number):
    result = score[i] / (M * 100)
    sum += result
    

a = (sum  * 10000) / number
print(a)
