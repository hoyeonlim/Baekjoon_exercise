from sys import stdin
from collections import deque
#
input = stdin.readline
n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
# visited = [ False for _ in range(n + 1)]
ans = [0 for _ in range(n + 1)]
for i in range(m):
    a, b = map(int, input().split())
    graph[b].append(a)

def bfs(start):
    queue = deque([start])
    cnt = 0
    visited = [False for _ in range(n + 1)]
    visited[start] = True
    while queue:
        value = queue.popleft()
        for z in graph[value]:
            if not visited[z]:
                visited[value] = True
                queue.append(z)
                cnt +=1
    return cnt

maxCnt = 1

for i in range(1, n+1):
    # ans[x] = bfs(x)
    cnt = bfs(i)
    if cnt > maxCnt:
        maxCnt = cnt
        ans.clear()
        ans.append(i)
    elif cnt == maxCnt:
        ans.append(i)

print(*ans)
# M = max(ans)
# for y in range(len(ans)):
#     if ans[y] == M:
#         print(y, end=' ')


#
# def dfs(seq, cnt):
#     cnt += 1
#     visited = [False] * (n+1)
#     visited[seq] = True
#
#     if len(graph[seq]) == 0:
#         temp.append(cnt)
#     else:
#         for x in graph[seq]:
#             if visited[x] == False:
#                 dfs(x, cnt)
#     return max(temp)
#
# for j in range(1, n+1):
#     temp = []
#     ans.append(dfs(j, 0))
#     # ans.append(max(temp))
#
# for x in range(len(ans)):
#     if ans[x] == max(ans):
#         print(x, end=' ')