n = int(input())
original = n
circle = 0

while(True):
    ten = n // 10
    one = n % 10
    sum = ten + one
    n = one * 10 + sum % 10
  
    circle += 1
    if n == original:
        break


print(circle)


# if n < 10:
#     n = n * 10


    # print(sum)
    # if sum < 10:
    #     result = (one * 10) + sum    
    # else:
    #     result = one * 10) + (sum % 10)



   # print(result)

    # if result != original:
    #     n = result
    # else:
    #     break