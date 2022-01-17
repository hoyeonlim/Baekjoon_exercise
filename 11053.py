import sys

n = int(sys.stdin.readline())
# arr = []
# ans = []
arr = list(map(int, sys.stdin.readline().split()))
ans = [arr[0]]

for j in range (1 ,n):
    if ans[-1] < arr[j]:
        ans.append(arr[j])
    else:
        cnt = 0
        for i in range(0, len(ans)):
            if ans[i] < arr[j]:
                cnt += 1
            else:
                ans[cnt] = arr[j]
                break

print(len(ans))
