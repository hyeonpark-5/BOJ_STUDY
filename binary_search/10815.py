n = int(input())
graph = list(map(int, input().split()))
m = int(input())
num = list(map(int, input().split()))
graph.sort()

def search(key):
    left = 0
    right = n - 1
    while True:
        mid = (left + right) // 2
        if graph[mid] == key:
            return 1
        elif graph[mid] < key:
            left = mid + 1
        else:
            right = mid - 1
            
        if left > right:
            break
    return '0'

for i in num:
    print(search(i), end = ' ')