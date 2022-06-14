from sys import stdin

arr = []
n, k = map(int, stdin.readline().split())
ans = []
id = 0
cnt = 1

for i in range(n+1):
    arr.append(i)

while True:
    if len(ans) == n:
        break
    if arr[id] != 0:
        if cnt == k and arr[id] != 0:
            ans.append(arr[id])
            arr[id] = 0
            cnt = 1
            continue
        elif cnt == k and arr[id] == 0:
            id += 1
            if id == n + 1:
                id %= n
            continue
        else:
            id += 1
            cnt += 1
            if id == n + 1:
                id %= n
    else:
        id += 1
        if id == n + 1:
            id %= n
        continue

print("<" + ', '.join(str(i) for i in ans) + ">", sep = '')