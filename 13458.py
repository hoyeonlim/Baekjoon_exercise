import math

n = int(input())
a = list(map(int, input().split()))
b, c = map(int, input().split())
super = []

for i in a:
    x = i-b
    if x <= 0:
        super.append(1)
    else:
        super.append(1 + math.ceil(x/c))
print(sum(super))