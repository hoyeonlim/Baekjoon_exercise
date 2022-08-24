from collections import deque
from sys import stdin

def bfs():
    while queue:
        order = queue.popleft()
        for i in graph[order]:
            if i not in queue:
                queue.append(i)
            ans[i] = min(ans[i], weight[order][i] + ans[order])


v, e = map(int, stdin.readline().split())
k = int(stdin.readline())
inf = 9999999
ans = [9999999 for _ in range(v + 1)]
queue = deque([])
queue.append(k)
ans[k] = 0

graph = [[] for _ in range(v + 1)]
weight = [[inf for _ in range(v + 1)] for _ in range(v + 1)]
visited = [False] * (v + 1)

for i in range (e):
    a, b, c = map(int, stdin.readline().split())
    graph[a].append(b)
    weight[a][b] = c

bfs()

for i in range(1, v + 1):
    if i == k:
        ans[i] = 0
    if ans[i] == inf:
        ans[i] = 'INF'
    print(ans[i])
