import sys
n = int(sys.stdin.readline())
arr = [0 for i in range(n)]

for j in range(n):
    arr[j] = int(sys.stdin.readline())
max = arr[n-1]
cnt = 1
for k in range(n-2, -1, -1):
    if arr[k] > max:
        max = arr[k]
        cnt += 1
    else:
        continue
print(cnt)
#EOF
#2022.01.24