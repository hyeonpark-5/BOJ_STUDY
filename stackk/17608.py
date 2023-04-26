import sys
input = sys.stdin.readline

stk = []
ptr = 0
result = 1
num  = int(input())

for i in range(0, num):
    n = int(input())
    stk.append(n)
    ptr += 1


max = stk[len(stk) - 1]
while ptr > 0 :
    a = stk.pop()
    if max > a or max == a:
        pass
    elif max < a:
        max = a
        result += 1
    ptr -= 1

print(result)

