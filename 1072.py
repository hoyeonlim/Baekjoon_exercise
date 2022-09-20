from sys import stdin
from math import floor
input = stdin.readline

x, y = map(int, input().split())

value = (y*100//x)

start = 0
end = 1000000000

if value == 99 or value == 100:
    print(-1)
else:
    while start <= end:
        mid = (start + end)//2
        ans = ((y + mid)) * 100 // (x + mid)
        if ans > value:
            end = mid - 1
        else:
            start = mid + 1
    print(end + 1)