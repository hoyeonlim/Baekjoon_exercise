from sys import stdin
input = stdin.readline

k, n = map(int, input().split())
arr = []

for i in range(k):
    arr.append(int(input()))

start = 1
end = max(arr)
# arr1 = sorted(arr)

while start <= end:
    cnt = 0
    mid = (start + end)//2
    for j in arr:
        cnt += j//mid
    if cnt >= n:
        start = mid + 1
    else:
        end = mid - 1
print(end)


