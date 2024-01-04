n = int(input())
meeting = []

for _ in range(n):
    s, e = map(int, input().split())
    meeting.append((s, e))
meeting.sort(key=lambda x:(x[1],x[0]))

end = 0
result = 0

for s, e in meeting:
    if s >= end:
        end = e
        result += 1
        
print(result)
