from collections import deque
from sys import stdin
def bfs(graph, visited, n):
    queue = deque([n])
    visited[n] = True
    cnt = 0
    while queue:
        ans = queue.popleft()
        for node in graph[ans]:
            if not visited[node]:
                queue.append(node)
                visited[node] = True
                cnt += 1
    return print(cnt)


n = int(stdin.readline())
arm = int(stdin.readline())
visited = [False] * (n + 1)
graph = [ [] for x in range(n+1)]

for i in range (arm):
    a, b = map(int, stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)


bfs(graph, visited, 1)