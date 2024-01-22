import sys
input = sys.stdin.readline


while True:
    s = input().rstrip()
    new = []
    answer = "yes"
    if s == '.':
        break
    elif s == '':
        continue
    for w in s:
        if w == '.':
            break
        if w.isalpha():
            continue
        else:
            if w == '(':
                new.append('(')
            elif w == '[':
                new.append('[')
            elif w == ')':
                if not new:
                    answer = 'no'
                elif new[-1] == '(':
                    new.pop()
                else:
                    answer = 'no'
            elif w == ']':
                if not new:
                    answer = 'no'
                elif new[-1] == '[':
                    new.pop()
                else:
                    answer = 'no'
            

    if len(new) == 0:
        print(answer)
    else:
        print('no') 