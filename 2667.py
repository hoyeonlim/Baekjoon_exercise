from collections import deque
from sys import stdin
n = int(stdin.readline())
graph = []

for i in range(n):
    graph.append(list(map(int, input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
ans = []

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    cnt = 1 #첫 카운트가 0이 아님에 주의
    graph[x][y] = 0 #첫번째 1 방문과 동시에 0으로 바꿔줌

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0 #방문한 자리를 0으로 처리
                cnt += 1
                queue.append((nx, ny))
    return cnt

for x in range(n):
    for y in range(n):
        if graph[x][y] == 1: #bfs()가 돌면 0으로 변하기 때문에 조건을 걸어준다
            ans.append(bfs(x, y))
ans.sort() #오름차순
print(len(ans))
for z in ans:
    print(z)