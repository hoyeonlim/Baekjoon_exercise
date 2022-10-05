from sys import stdin

input = stdin.readline

n, k = map(int, input().split())
arr = []
dp = [1000000 for _ in range(k + 1)]
dp[0] = 0
for i in range(n):
    arr.append(int(input()))

for m in arr:
    for l in range(m, k + 1):
        dp[l] = min(dp[l], dp[l - m] + 1)

if dp[k] == 1000000:
    print(-1)
else:
    print(dp[k])
