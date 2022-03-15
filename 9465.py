from sys import stdin

n = int(stdin.readline())
for i in range(n):
    a = int(stdin.readline())
    # b = []
    # c = []
    for j in range(1):
        b = list(map(int,stdin.readline().split()))
        c = list(map(int,stdin.readline().split()))
        for k in range(1, a):
            if k == 1:
                b[k] = c[k-1] + b[k]
                c[k] = b[k-1] + c[k]
            else:
                b[k] = max(c[k-1]+b[k], c[k-2]+b[k])
                c[k] = max(b[k-1]+c[k], b[k-2]+c[k])
        print(max(b[a-1], c[a-1]))