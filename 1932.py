import sys

n = int(sys.stdin.readline())
tri = []

for x in range (0 ,n):
    tri.append(list(map(int, sys.stdin.readline().split())))

dp = tri

for i in range(1, n):
    for j in range(0, i+1):
        if j == 0:
            dp[i][j] = dp[i-1][j] + dp[i][j]
        elif j == i:
            dp[i][j] = dp[i-1][j-1] + dp[i][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-1]) + dp[i][j]

print(max(max(dp)))