from sys import stdin
from math import sqrt
input = stdin.readline

n = int(input())
dp = [0 for _ in range(n + 1)]
arr = []
num = int(sqrt(n))


for i in range(1, num + 1):
    # dp[i**2] = 1
    arr.append(i**2)

for i in range(1, n + 1):
    temp = []
    for j in arr:
        dp[j] = 1
        if i < j:
            break
        temp.append(dp[i - j])
    dp[i] = min(temp) + 1

print(dp[n])


