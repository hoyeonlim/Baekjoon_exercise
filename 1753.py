from sys import stdin
from heapq import heappop, heappush

input = stdin.readline
V, e = map(int, input().split())
k = int(input())
graph = [[] for _ in range(V + 1)]
ans = [3000001 for _ in range(V + 1)]

for i in range(e):
    u, v, w = map(int, input().split())
    graph[u].append([v, w])


def dikstra(start):
    ans[start] = 0
    heap = []
    heappush(heap, [0 ,start])
    while heap:
        w, d = heappop(heap)
        if ans[d] < w:
            continue
        for j, k in graph[d]:
            if ans[j] > ans[d] + k:
                ans[j] = ans[d] + k
                heappush(heap, [k, j])

dikstra(k)

for x in range(1, V+1):
    if ans[x] == 3000001:
        print("INF")
    else:
        print(ans[x])
