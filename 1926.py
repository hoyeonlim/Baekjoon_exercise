from sys import stdin
from collections import deque

input = stdin.readline

def dfs(i, j):
    cnt = 1
    queue = deque()
    queue.append((i, j))
    graph[i][j] = 0

    while queue:
        x, y = queue.popleft()
        for _ in range(4):
            nx = x + dx[_]
            ny = y + dy[_]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append((nx, ny))
                cnt += 1
    return cnt

n, m = map(int, input().split())
graph = []
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
# answer = [[0 for _ in range(m)] for _ in range(n)]
answer = []

for i in range(n):
    graph.append(list(map(int, input().split())))

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            answer.append(dfs(i, j))

if len(answer) == 0:
    print(0, 0, sep ='\n')
else:
    print(len(answer), max(answer), sep = '\n')
