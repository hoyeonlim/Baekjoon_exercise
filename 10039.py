import sys
sum = 0
for i in range(0, 5):
    x = int(sys.stdin.readline())
    if x < 40:
        x = 40
    sum += x

print(int(sum/5))