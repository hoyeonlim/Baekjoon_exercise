from sys import stdin
n = int(stdin.readline())
arr = []
dp = [[0 for i in range(3)] for i in range(n)]
for i in range(n):
    arr.append(list(map(int, stdin.readline().split())))
# dp[0] = arr[0]
dp[0][0] = arr[0][0]
dp[0][1] = arr[0][1]
dp[0][2] = arr[0][2]
for j in range(1, n):
    dp[j][0] = min(dp[j-1][1] + arr[j][0], dp[j-1][2] + arr[j][0])
    dp[j][1] = min(dp[j-1][0] + arr[j][1], dp[j-1][2] + arr[j][1])
    dp[j][2] = min(dp[j-1][0] + arr[j][2], dp[j-1][1] + arr[j][2])
print(min(dp[n-1]))