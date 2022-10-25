from sys import stdin
from heapq import heappop, heappush
input = stdin.readline

n = int(input())
arr = []

for i in range(n):
    x = int(input())
    if x > 0:
        heappush(arr, (-x, x))
    else:
        if len(arr) == 0:
            print(0)
        else:
            print(heappop(arr)[1])