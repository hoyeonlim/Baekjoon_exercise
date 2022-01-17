import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
sum = [0] * len(arr)
sum[0] = arr[0]

for i in range(1, n):
    sum[i] = max(arr[i], sum[i-1]+arr[i])
print(max(sum))
