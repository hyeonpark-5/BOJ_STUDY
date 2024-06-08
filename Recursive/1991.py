# 트리 순회
def preorder(w):
    if w == '.':
        return
    print(w, end ='')
    preorder(tree[w][0])
    preorder(tree[w][1])

def inorder(w):
    if w == '.':
        return 
    inorder(tree[w][0])
    print(w, end='')
    inorder(tree[w][1])

def postorder(w):
    if w == '.':
        return 
    postorder(tree[w][0])
    postorder(tree[w][1])
    print(w, end ='')
n = int(input())
tree = {}
for _ in range(n):
    root, left, right = input().split()
    tree[root] = [left, right]

preorder('A')
print()
inorder('A')
print()
postorder('A')

