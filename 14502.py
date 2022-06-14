from collections import deque
from sys import stdin
import copy

def bfs():
    queue = deque()
    graph2 = copy.deepcopy(graph)
    # graph2[a//m][a%m] = 1
    # graph2[b//m][b%m] = 1
    # graph2[c//m][c%m] = 1
    cnt = 0
    line2 = []
    for i in range(n):
        for j in range(m):
            if graph2[i][j] == 2:
                queue.append((i, j))
                # print(graph2[i][j])
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if graph2[nx][ny] == 1:
                continue
            if graph2[nx][ny] == 0:
                graph2[nx][ny] = 2
                queue.append((nx, ny))

    for i in range(n):
        for j in graph2[i]:
            line2.append(str(j))
    wall = line2.count('1')
    virus = line2.count('2')
    ans = n * m - wall - virus
    answer.append(ans)
    return

def makewall(cnt):
    if cnt == 3:
        bfs()
        return

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                graph[i][j] = 1
                makewall(cnt+1)
                graph[i][j] = 0

n, m = map(int, stdin.readline().split())
graph = []
line = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
answer = []

for j in range(n):
    graph.append(list(map(int, stdin.readline().split())))
for i in range(n):
    for j in graph[i]:
        line.append(j)

# for a in range(len(line)-3):
#     if line[a] == 0:
#         for b in range(a+1, len(line)-2):
#             if line[b] == 0:
#                 for c in range(b+1, len(line)-1):
#                     if line[c] == 0:
#                         bfs()
#                     else:
#                         continue
#             else:
#                 continue
#     else:
#         continue
makewall(0)
print(max(answer))