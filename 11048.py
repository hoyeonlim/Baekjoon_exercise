from sys import stdin
input = stdin.readline

n, m = map(int, input().split())
arr = []
dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
dx = [-1, -1, 0]
dy = [0, -1, -1]

for i in range(n):
    arr.append(list(map(int, input().split())))

for i in range(1, n + 1):
    for j in range(1, m + 1):
        for k in range(3):
            x = j + dx[k]
            y = i + dy[k]
            if not 0 <= x <= m or not 0 <= y <= n:
                continue
            if dp[i][j] < dp[y][x] + arr[i - 1][j - 1]:
                dp[i][j] = dp[y][x] + arr[i - 1][j - 1]

print(dp[-1][-1])