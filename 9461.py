from sys import stdin
t = int(stdin.readline())
dp = [0 for i in range(100)]
dp[0] = 1
dp[1] = 1
dp[2] = 1
dp[3] = 2
dp[4] = 2
for i in range (t):
    n = int(stdin.readline())
    if n >= 5:
        for j in range(5, n):
            dp[j] = dp[j-1] + dp[j-5]
        print(dp[n-1])
    else:
        print(dp[n-1])
#9461
