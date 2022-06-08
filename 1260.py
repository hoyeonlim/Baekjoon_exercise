from collections import deque
from sys import stdin

def dfs(visited, graph, v):
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(visited, graph, i)

def bfs(visited, graph, v):
    queue = deque([v])
    visited[v] = True
    while queue:
        a = queue.popleft()
        print(a, end=' ')
        for i in graph[a]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

n, m, v = map(int, stdin.readline().split())
graph = [[] for i in range(n+1)]
visited = [False] * (n+1)

for i in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

for j in range(len(graph)):
    graph[j].sort()

dfs(visited, graph, v)
visited = [False] * (n+1)
print()
bfs(visited, graph, v)