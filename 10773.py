import sys
k = int(sys.stdin.readline())
arr = []
for i in range(0 ,k):
    j = int(sys.stdin.readline())
    if j == 0:
        arr.pop(-1)
        continue
    else:
        arr.append(j)
print(sum(arr))