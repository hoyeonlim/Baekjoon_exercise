from sys import stdin
from heapq import heappop, heappush

input = stdin.readline
n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
ans = [100000001 for _ in range(n+1)]

for i in range(m):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])

start, end = map(int, input().split())

def dik(start):
    ans[start] = 0
    heap = []
    heappush(heap, [0, start])
    while heap:
        x, y = heappop(heap)
        if ans[y] < x:
            continue
        for a, b in graph[y]:
            if ans[a] > x + b:
                ans[a] = x + b
                heappush(heap, [x + b, a])



dik(start)
print(ans[end])