from sys import stdin

n, k = map(int, stdin.readline().split())
arr = [[0, 0]]
sum = 0
dp = [[0 for x in range(k+1)] for y in range(n+1)]

for i in range(n):
    arr.append(list(map(int, stdin.readline().split())))

for i in range(1, n+1):
    for j in range(1, k+1):
        w = arr[i][0]
        v = arr[i][1]
        if j < w:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-w]+v)
print(max(max(dp)))