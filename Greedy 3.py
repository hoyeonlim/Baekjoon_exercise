from sys import stdin

n, m = map(int, stdin.readline().split())
result = 0

for i in range(n):
    arr = list(map(int, stdin.readline().split()))
    minv = min(arr)
    result = max(minv, result)

print(result)