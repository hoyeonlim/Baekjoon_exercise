from sys import stdin
import heapq
input = stdin.readline

n = int(input())
cnt = 0
arr = [0 for _ in range(n)]
for i in range(n):
    arr[i] = int(input())

heapq.heapify(arr)
while True:
    minv1 = heapq.heappop(arr)
    minv2 = heapq.heappop(arr)
    heapq.heappush(arr, minv1 + minv2)
    cnt += minv1 + minv2
    # minv1 = min(arr)
    # arr.remove(minv1)
    # minv2 = min(arr)
    # arr.remove(minv2)
    # arr.append(minv1 + minv2)
    # cnt += minv1 + minv2          ###시간초과!
    print(arr)
    if len(arr) == 1:
        break
print(cnt)