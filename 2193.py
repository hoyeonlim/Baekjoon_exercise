from sys import stdin
n = int(stdin.readline())
dp = [[0 for i in range(2)] for i in range(n)]

dp[0] = [0, 1]

for x in range(1, n):
    dp[x][0] = dp[x-1][0] + dp[x-1][1]
    dp[x][1] = dp[x-1][0]
print(sum(dp[n-1]))