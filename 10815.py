from sys import stdin

input = stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr1 = sorted(arr)
m = int(input())
arr2 = list(map(int, input().split()))
ans = []

def binary(array, value, start, end):
    cnt = 0
    if start > end:
        return 0
    mid = (start + end) // 2
    if array[mid] == value:
        return 1
    if array[mid] < value:
        return binary(arr1, value, mid + 1, end)
    if array[mid] > value:
        return binary(arr1, value, start, mid - 1)

for i in arr2:
    ans.append(binary(arr1, i, 0, n-1))
print(*ans)