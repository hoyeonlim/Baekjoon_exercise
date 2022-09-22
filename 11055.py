from sys import stdin

input = stdin.readline

n = int(input())
A = list(map(int, input().split()))
dp = [0 for _ in range(n+1)]
dp[1] = A[0]

for i in range(1, n):
    temp = []
    for j in range(0, i):
        if A[i] > A[j]:
            temp.append(dp[j + 1])
    if bool(temp) == True:
        dp[i + 1] = A[i] + max(temp)
    else:
        dp[i + 1] = A[i]

print(max(dp))