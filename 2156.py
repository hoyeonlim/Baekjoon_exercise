from sys import stdin
n = int(stdin.readline())
arr = []
ans = [0]

for i in range(0, n):
    arr.append(int(stdin.readline()))
if n > 1:
    ans.append(arr[0])
    ans.append(arr[0] + arr[1])

for j in range(3, n+1):
    ans.append(max(ans[j-1], ans[j-2] + arr[j-1], ans[j-3] + arr[j-1] + arr[j-2]))
print(ans[n])