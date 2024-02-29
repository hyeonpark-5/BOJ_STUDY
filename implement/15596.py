strr = input()
original = int(strr)
circle = 0
# ten = int(strr[0])
# one = int(strr[1])
while(True):
    ten = int(strr[0])
    one = int(strr[1])
    if one < 10:
        one = one * 10
    sum = ten + one
    result = one * 10 + (sum % 10)
    circle += 1
    print(result)
    if result != original:
        strr = str(result)
    else:
        break


print(circle)
