from sys import stdin
input = stdin.readline

n = int(input())
arr = sorted(list(map(int, input().split())))
m = int(input())
piece = 0
middle = m//n
start = 0
end = len(arr) - 1
cnt = 0
sum = 0
while start < end:
    mid = (start + end)//2
    if middle > arr[mid]:
        start = mid + 1
    elif middle < arr[mid]:
        end = mid - 1

while cnt <= end:
    sum += (middle - arr[cnt])
    cnt += 1

ans = sum//(len(arr) - start)
print(min(arr[-1], middle + ans))