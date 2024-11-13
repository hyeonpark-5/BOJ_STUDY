n = int(input())
tree = list(int(input()) for _ in range(n))
new_tree = []
result = 0
def newgcd(x, y):
    while y:
        x, y = y, x % y
    return x

for i in range(n - 1):
    new_tree.append(tree[i + 1] - tree[i])

gcd = new_tree[0]
for i in range(1, len(new_tree)):
    gcd = newgcd(gcd, new_tree[i])

for i in new_tree:
    result += i // gcd - 1

print(result)