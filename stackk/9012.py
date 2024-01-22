n = int(input())

for _ in range(n):
    s = input()
    stack = []
    answer = "YES"
    for w in s:
        if w == '(':
            stack.append(w)
        else:
            if not stack:
                answer = "NO"
                break
            stack.pop()
    
    if len(stack) != 0:
        print("NO")
    else:
        print(answer)