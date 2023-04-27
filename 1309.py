from sys import stdin
import copy

n = int(stdin.readline())

dp = [[1, 1, 1] for _ in range(2)]

for i in range(1, n):
    dp[1][0] = dp[0][0] + dp[0][1] + dp[0][2]
    dp[1][1] = dp[0][0] + dp[0][2]
    dp[1][2] = dp[0][0] + dp[0][1]
    dp[0] = copy.deepcopy(dp[1])

print(sum(dp[1])%9901)
