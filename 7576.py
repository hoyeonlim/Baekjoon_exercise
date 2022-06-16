from collections import deque
from sys import stdin

def bfs():
    while queue:
        y, x = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= m or ny >= n:
                continue
            if box[ny][nx] == -1:
                continue
            if box[ny][nx] == 0:
                box[ny][nx] = box[y][x] + 1
                queue.append((ny, nx))


m, n = map(int, stdin.readline().split())
box = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
queue = deque([])
cnt = 0
des = True

for i in range(n):
    box.append(list(map(int, stdin.readline().split())))

for i in range(n):
    for j in range(m):
        if box[i][j] == 1:
            queue.append([i, j])
bfs()
# print(box)
for x in box:
    for j in x:
        if j == 0:
            print(-1)
            des = False
            break
    if des == False:
        break
    cnt = max(cnt, max(x))
if des == True:
    print(cnt-1)