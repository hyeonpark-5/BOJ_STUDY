f = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

while True:
    n = input()
    sum = 0

    if n == '#':
        break

    for i in f:
        sum += n.count(i)

    print(sum)