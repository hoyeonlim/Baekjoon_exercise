from sys import stdin
input = stdin.readline

n = int(input())
arr = list(map(int, input().split()))
dp = [1 for _ in range(n + 1)]

for i in range(1, n):
    temp = set()
    for j in range(0, i):
        if arr[i] < arr[j]:
            temp.add(arr[j])
    if len(temp) > 0:
        dp[i + 1] = min(dp) + len(temp)
    else:
        dp[i + 1] = min(dp)

print(max(dp))
