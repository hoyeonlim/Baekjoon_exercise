from sys import stdin

input = stdin.readline

n = int(input())
arr = list(map(int, input().split()))
m = int(input())

start = 1
end = max(arr)

while start <= end:
    mid = (start + end) // 2
    sum = 0
    for j in arr:
        if j >= mid:
            sum += mid
        else:
            sum += j
    if sum <= m:
        start = mid + 1
    else:
        end = mid - 1
print(end)