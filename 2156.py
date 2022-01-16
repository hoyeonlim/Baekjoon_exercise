from sys import stdin
n = int(stdin.readline())
arr = []
p1 = 0
p2 = 1
p3 = 3
ans = []

for i in range(0, n):
    arr.append(int(stdin.readline()))

for j in range (0 ,n):
    ans.append(arr[p1] + arr[p2] + arr[p3])
