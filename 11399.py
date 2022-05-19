from sys import stdin

n = int(stdin.readline())
p = list(map(int, stdin.readline().split()))
sum = 0

for i in range(n):
    sum += (i+1)*max(p)
    p.remove(max(p))

print(sum)