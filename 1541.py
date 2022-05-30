a = input().split('-')
b = []
c = []

for x in a:
    b = x.split('+')
    total = 0
    for y in b:
        total += int(y)
    c.append(total)

sum = c[0] * 2
for z in c:
    sum -= z
print(sum)