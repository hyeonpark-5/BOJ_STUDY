t = int(input())

for _ in range(t):
    n = int(input())
    dp = [0] * (n + 1)
    if n < 6:
        if n < 4:
            print(1)
        else:
            print(2)
        continue
    
    dp[1] = 1
    dp[2] = 1
    dp[3] = 1
    dp[4] = 2
    dp[5] = 2
    j = 1
    for i in range(6, n + 1): 
        dp[i] = dp[i - 1] + dp[j]
        j += 1
        
    print(dp[n])