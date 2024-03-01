h, m = map(int,input().split())
cook = int(input())

if m + cook >= 60:
    m = m + cook - 60
    if m >= 60:
        h += 1
        m = 0

    h += 1
    if h >= 23:
        h = 0
    

else:
    m += cook
    if m >= 60:
        h += 1
        m = 0
        
    if h >= 23:
        h += 1
        h = 0

print(f"{h} {m}")


