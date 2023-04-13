from sys import stdin

input = stdin.readline

a, b = map(int, input().split())
cnt = 0
while b > a:
    if b % 2 == 0:
        b = b//2
        cnt += 1
    elif b % 10 == 1:
        b = (b - 1)//10
        cnt += 1
    elif (b % 2 != 0) and (b % 10 != 1):
        break

if a == b:
    print(cnt + 1)
else:
    print(-1)
