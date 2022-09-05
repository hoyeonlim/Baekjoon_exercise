import sys
from sys import stdin
input = stdin.readline
from collections import deque
sys.setrecursionlimit(10**9)

n = int(input())
arr = [[] for _ in range(n+1)]
ans = [ 0 for _ in range(n+1)]
visited = [False] * (n+1)
queue = deque([])
visited[1] = True

for i in range(1, n):
    x, y = map(int, input().split())
    arr[x].append(y)
    arr[y].append(x)

def bfs(x):
    for i in arr[x]:
        if visited[i] == False:
            queue.append(i)
            visited[i] = True
            ans[i] = x
    while queue:
        a = queue.popleft()
        bfs(a)

bfs(1)
# for z in range(2, n+1):
#     print(ans[z])