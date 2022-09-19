from sys import stdin

input = stdin.readline
n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
ans = [0]

for i in range(m):
    a, b = map(int, input().split())
    graph[b].append(a)

def dfs(seq, cnt):
    cnt += 1
    visited = [False] * (n+1)
    visited[seq] = True

    if len(graph[seq]) == 0:
        temp.append(cnt)
    else:
        for x in graph[seq]:
            if visited[x] == False:
                dfs(x, cnt)
    return max(temp)

for j in range(1, n+1):
    temp = []
    ans.append(dfs(j, 0))
    # ans.append(max(temp))

for x in range(len(ans)):
    if ans[x] == max(ans):
        print(x, end=' ')