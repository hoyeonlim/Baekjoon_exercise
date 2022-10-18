from sys import stdin
from collections import deque

input = stdin.readline

t = int(input())

for i in range(t):
    p = input()
    n = int(input())
    pl = list(p.strip())
    arr = input().strip()[1:-1].split(',')
    if n == 0:
        arr = deque()
    else:
        arr = deque(arr)
    state = 1
    cnt = 0
    for j in range(len(pl)):
        if pl[j] == 'R':
            cnt += 1
        else:
            if len(arr) == 0:
                print("error")
                state = 2
                break
            if cnt % 2 == 1:
                arr.pop()
            else:
                arr.popleft()

    if state == 1:
        if cnt % 2 == 1:
            arr.reverse()
            print('[' + (',').join(arr) + ']')
        else:
            print('[' + (',').join(arr) + ']')