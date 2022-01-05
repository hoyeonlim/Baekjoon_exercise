import sys
# n = int(input())
#
# for x in range (0, n):
#     a = int(input())
#     f = list(0 for i in range(0, a+1))
#     f[1] = 1
#     f[2] = 2
#     f[3] = 4
#     for y in range (4, a+1):
#         f[y] = f[y-1] + f[y-2] + f[y-3]
#     print(f[a])
def f(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    else:
        return f(n-1) + f(n-2) + f(n-3)
n = int(sys.stdin.readline())

for x in range (0, n):
    y = int (sys.stdin.readline())
    print(f(y))