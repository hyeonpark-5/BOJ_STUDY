number = int(input())
count = 0

while number >= 0:
    if number % 5 == 0:
        count += int(number // 5)
        print(count)
        break
    number -= 3
    count += 1

else:
    print(-1)


# if kg_5_last != 0 and kg_3_last != 0:
#     print(-1)
# else:
#     if kg_5_last % 3 == 0:
#         result = kg_5 + (kg_5_last // 3)
#     else:
#         result = number // 3

#     print(result)




        



    
 
# 5로 나눴을 때 나머지가 3의 배수인가
# 안되면 3으로 나누기 시작






