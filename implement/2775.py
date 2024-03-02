#부녀회장이 될테야
t = int(input())

for _ in range(t):
    k = int(input()) #층
    n = int(input()) # 호수
    dp = [[1] * n for _ in range(k + 1)]
    for i in range(n):
        dp[0][i] = i + 1
   

    for i in range(1, k + 1):
        for j in range(1, n):
            dp[i][j] = dp[i][j - 1] + dp[i - 1][j]
    
    print(dp[k][n - 1])