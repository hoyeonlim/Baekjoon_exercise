from sys import stdin

input = stdin.readline

n = int(input())
x, y = map(int, input().split())
m = int(input())

arr = [[] for _ in range(n+1)]
visited = [False] * (n+1)
answer = []
### Make graph ###
for i in range(m):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

def dfs(ans, cnt):
    cnt += 1
    visited[ans] = True

    if ans == y:
        answer.append(cnt)

    for i in arr[ans]:
        if visited[i] == False: # check visited log
            dfs(i, cnt) # dfs recursion
        
dfs(x, 0)

if len(answer) == 0:
    print(-1)
else:
    print(answer[-1]-1)