from sys import stdin
n = int(stdin.readline())
t = []
p =[]
dp = [0 for i in range(n+1)]
for i in range (n):
    com = list(map(int, stdin.readline().split()))
    t.append(com[0])
    p.append(com[1])

for i in range(n-1,-1,-1):
    if i + t[i] > n:
        dp[i] = dp[i+1]
    else:
        dp[i] = max(dp[i+1], dp[i+t[i]] + p[i])
print(dp[0])
