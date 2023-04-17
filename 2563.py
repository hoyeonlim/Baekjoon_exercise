from sys import stdin

n = int(stdin.readline())
# array = [[] for _ in range(n)]
# answer = []
# value = 100 * n
#
# for i in range(n):
#     array[i] = list(map(int, stdin.readline().split()))
#
# for x in range(n-1):
#     for y in range(x+1, n):
#         difx = abs(array[x][0] - array[y][0])
#         dify = abs(array[x][1] - array[y][1])
#         if (difx < 10) and (dify < 10):
#             answer.append((10-difx) * (10-dify))
#
# print(value - sum(answer))
### 3장이상 곂칠 때 에러 발생 ###

graph = [[0 for _ in range(101)] for _ in range(101)]
array = [[] for _ in range(n)]
answer = 0

for i in range(n):
    array[i] = list(map(int, stdin.readline().split()))

for z in range(n):
    x = array[z][0]
    y = array[z][1]
    for i in range(x, x+10):
        for j in range(y, y+10):
            graph[i][j] = 1

for cnt in range(101):
    answer += graph[cnt].count(1)

print(answer)
