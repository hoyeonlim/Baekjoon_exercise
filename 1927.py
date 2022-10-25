from sys import stdin
from heapq import heappush, heappop

input = stdin.readline

n = int(input())
heapq = []

for i in range(n):
    num = int(input())
    if num == 0:
        if len(heapq) == 0:
            print(0)
        else:
            print(heappop(heapq))
    else:
        heappush(heapq, num)
