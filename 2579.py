from sys import stdin

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
print(ans)
print(ans[n-1])