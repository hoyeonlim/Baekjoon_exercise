from sys import stdin
<<<<<<< HEAD

n = int(stdin.readline())
arr = []
ans = [0]*(n+1)

for i in range (0 ,n):
    arr.append(int(stdin.readline()))

ans[0] = arr[0]
ans[1] = arr[0] + arr[1]
ans[2] = max(arr[1]+arr[2], arr[0]+arr[2])

for j in range (3, n):
    ans[j] = max(ans[j-3]+arr[j-1]+arr[j], ans[j-2]+arr[j])

print(ans[n-1])
=======
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
>>>>>>> 5aa4bfc8145fe902f0e3c86660b18eea440c09d2
