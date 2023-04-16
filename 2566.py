from sys import stdin
graph = [[] for _ in range(10)]
maxnum = 0

for i in range(1,10):
    graph[i] = list(map(int, stdin.readline().split()))
    graph[i].insert(0, 0)

for x in range(1, 10):
    for y in range(1, 10):
        if maxnum <= graph[x][y]:
            maxnum = graph[x][y]
            posix = x
            posiy = y

print(maxnum)
print(posix, posiy, sep=' ')


