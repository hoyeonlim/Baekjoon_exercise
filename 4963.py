from collections import deque
from sys import stdin

def bfs():
    cnt = 1
    while queue:
        x, y = queue.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= w or ny >= h:
                continue
            if graph[ny][nx] == 0:
                continue
            if graph[ny][nx] == 1:
                graph[ny][nx] = 0
                cnt += 1
                queue.append((nx, ny))
    return cnt

dx = [1, 1, 1, -1, -1, -1, 0, 0]
dy = [1, 0, -1, 1, 0, -1, 1, -1]


while True:
    w, h = map(int, stdin.readline().split())
    graph = []
    queue = deque([])
    ans = []
    if w == 0 and h == 0:
        break
    for i in range(h):
        graph.append(list(map(int, stdin.readline().split())))
    for a in range (h):
        for b in range(w):
            if graph[a][b] == 1:
                queue.append([b, a])
                ans.append(bfs())
    print(len(ans))
