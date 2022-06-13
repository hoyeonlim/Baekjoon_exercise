from collections import deque
from sys import stdin

def bfs(a):
    if visited[a]:
        return False
    queue = deque([a])
    visited[a] = True
    cnt = 0
    while queue:
        node = queue.popleft()
        for x in arr[node]:
            if not visited[x]:
                queue.append(x)
                cnt += 1
                visited[x] = True
    return ans.append(cnt)


n, m = map(int, stdin.readline().split())
arr = [[] for _ in range(n+1)]
visited = [False] * (n+1)
ans = []

for i in range(m):
    u, v = map(int, stdin.readline().split())
    arr[u].append(v)
    arr[v].append(u)

for j in range(1, n+1):
    bfs(j)
print(len(ans))