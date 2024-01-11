n = input()
n = n.lower()
num = {}
for i in n:
    if i in num:
        num[i] += 1
    else:
        num[i] = 1

new = sorted(num.items(), key = lambda x:x[1], reverse=True)

if len(new) == 1 or new[0][1] != new[1][1]:
    print(new[0][0].upper())
else:
    print('?')