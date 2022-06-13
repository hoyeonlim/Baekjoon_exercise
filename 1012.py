from collections import deque
from sys import stdin

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    cnt = 1
    graph[y][x] = 0
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= m or ny >= n:
                continue
            if graph[ny][nx] == 0:
                continue
            if graph[ny][nx] == 1:
                graph[ny][nx] = 0
                cnt += 1
                queue.append((nx, ny))
    return cnt

t = int(stdin.readline())
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for a in range(t):
    m, n, k = map(int, stdin.readline().split())
    ans = []
    graph = [ [0 for _ in range(m)] for _ in range(n)]
    for b in range(k):
        x, y = map(int, stdin.readline().split())
        graph[y][x] = 1
    for y in range(n):
        for x in range(m):
            if graph[y][x] == 1:
                ans.append(bfs(x, y))
    print(len(ans))




