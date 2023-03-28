n, k = map(int, input().split())

def fectorial(a):
    total = 1
    for i in range(a,0,-1):
        total *= i
    
    return total


result = fectorial(n) / (fectorial(k) * fectorial(n-k))
print(int(result))
