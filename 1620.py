from sys import stdin
input = stdin.readline

n, m = map(int, input().split())
arr = {}
arr2 = {}
for i in range(n):
    x = input().strip()
    arr[i] = x
    arr2[x] = i

for j in range(m):
    x = input().strip()
    if x.isdigit():
        print(arr[int(x) - 1])
    else:
        print(arr2[x] + 1)