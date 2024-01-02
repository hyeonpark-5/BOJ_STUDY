k, n = map(int, input().split())
line = []
large = 0
result = 0
def find(len):
    count = 0
    for s in line:
        count += s // len
    return count

for _ in range(k):
    length = int(input())
    line.append(length)

large = max(line)
start = 1
end = large
while start <= end:
    mid = (start + end) // 2
    if find(mid) >= n:
        result = mid
        start = mid + 1
    else:
        end = mid - 1

print(result)