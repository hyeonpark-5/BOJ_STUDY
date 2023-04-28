import sys
input = sys.stdin.readline

n = int(input())
stk = []
for i in range(0, n):
    st = int(input())
    if st == 0:
        stk.pop()
    else:
        stk.append(st)


print(sum(stk))
    

