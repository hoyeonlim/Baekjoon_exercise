from sys import stdin
from heapq import heappop,heappush
input = stdin.readline

n = int(input())
arr = []
answer = []

for i in range(n):
    a, b = map(int, input().split())
    heappush(arr, [a, b])

arr.sort()
heappush(answer, arr[0][1])
cnt = 1

for j in range(1, n):
    if arr[j][0] < answer[0]:
        heappush(answer, arr[j][1])
        cnt += 1
    else:
        heappop(answer)
        heappush(answer, arr[j][1])

print(cnt)