import copy
from sys import stdin
from collections import deque

def bfs():
    cnt = 1
    while queue:
        c, d = queue.popleft()
        for i in range(4):
            nc = c + dx[i]
            nd = d + dy[i]
            if nc < 0 or nd < 0 or nc >= n or nd >= n:
                continue
            if graph1[nd][nc] == 0:
                continue
            if graph1[nd][nc] != 0:
                graph1[nd][nc] = 0
                cnt += 1
                queue.append((nc, nd))
    return cnt


sr = stdin.readline
n = int(sr())
graph = []
graph1 = []
answer = []

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


for i in range(n):
    graph.append(list(map(int, sr().split())))

minv = min(min(graph))
maxv = max(max(graph))

for x in range(0, maxv):
    queue = deque([])
    ans = []
    for y in range(n):
        for z in range(n):
            if graph[y][z] <= x:
                graph[y][z] = 0
    graph1 = copy.deepcopy(graph)
    #print(graph, graph1, sep='\n')
    for a in range(n):
        for b in range(n):
            if graph1[a][b] != 0:
                queue.append([b, a])
                ans.append(bfs())
    answer.append(len(ans))
print(max(answer))

