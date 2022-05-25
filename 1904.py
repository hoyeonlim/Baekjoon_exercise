from sys import stdin

n = int(stdin.readline())
dp = [0] * 10001

dp[1] = 1
dp[2] = 2
for x in range(3, n+1):
    dp[x] = (dp[x-1] + dp[x-2])%15746

print(dp[n])