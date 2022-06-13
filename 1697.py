from sys import stdin
from collections import deque


def bfs(n, k):
    queue = deque([n])

    while queue:
        node = queue.popleft()
        if node == k:
            return print(cnt[node])
            break
        for y in (node - 1, node + 1, node * 2):
            if 0 <= y <= 100000 and not cnt[y]:
                cnt[y] = cnt[node] + 1
                queue.append(y)


n, k = map(int, stdin.readline().split())
cnt = [0] * 100001

bfs(n, k)