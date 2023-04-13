from sys import stdin
input = stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
dp = [[0 for _ in range(n)] for _ in range(n)]
dp[0][0] = 1
dx = [1, 0]
dy = [0, 1]

for i in range(n):
    for j in range(n):
        if i == n - 1 and j == n - 1:
            print(dp[i][j])
            break
        if j + arr[i][j] < n :                      ### solve 1 ###
            dp[i][j + arr[i][j]] += dp[i][j]
        if i + arr[i][j] < n :
            dp[i + arr[i][j]][j] += dp[i][j]

        # for k in range(2):                        ### solve 2 ###
        #     x = j + dx[k]*arr[i][j]
        #     y = i + dy[k]*arr[i][j]
        #     if x >= n or y >= n:
        #         continue
        #     print(i,j, x, y)
        #     dp[y][x] += dp[i][j]