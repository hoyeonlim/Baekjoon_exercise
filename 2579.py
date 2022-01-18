from sys import stdin
n = int(stdin.readline())
arr = [0]*n
dp = []
for i in range(0, n):
    arr.append(int(stdin.readline()))

if n > 2:
    dp.append(arr[0])
    dp.append(arr[0]+arr[1])
    dp.append(max(arr[0]+arr[2], arr[1]+arr[2]))

for j in range (3, n):
    dp.append(max(dp[j-2]+arr[j], dp[j-3]+arr[j]+arr[j-1]))

print(dp[n-1])