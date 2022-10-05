from sys import stdin
input = stdin.readline

n = int(input())
arr = list(map(int, input().split()))

dpf = [0 for _ in range(n)] ### dp forward  ###
dpb = [0 for _ in range(n)] ### dp backward ###
dps = [0 for _ in range(n)] ### dp sum      ###

for i in range(n):
    for j in range(i):
        if arr[i] > arr[j] and dpf[j] > dpf[i]:
            dpf[i] = dpf[j]
    dpf[i] += 1

for x in range(n - 1, -1, -1):
    for y in range(n - 1, x, -1):
        if arr[x] > arr[y] and dpb[y] > dpb[x]:
            dpb[x] = dpb[y]
    dpb[x] += 1

for z in range(n):
    dps[z] = dpf[z] + dpb[z]

print(max(dps) - 1)