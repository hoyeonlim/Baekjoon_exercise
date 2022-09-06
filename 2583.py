from sys import stdin
from collections import deque

input = stdin.readline
m, n, k = map(int, input().split())
graph = [[0 for _ in range(n)] for _ in range(m)]
ans = []
queue = deque([])
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs():
    cnt = 1
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if graph[ny][nx] == 1:
                continue
            if graph[ny][nx] == 0:
                graph[ny][nx] = 1
                cnt += 1
                queue.append((nx, ny))
    return cnt

for i in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    for j in range(x1, x2):
        for k in range(y1, y2):
            graph[k][j] = 1


for y in range(m):
    for x in range(n):
        if graph[y][x] == 0:
            graph[y][x] = 1
            queue.append([x, y])
            ans.append(bfs())
print(len(ans))
ans.sort()
print(*ans, sep=' ')
