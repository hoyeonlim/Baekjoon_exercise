n = int(input())
cnt = 0

if n == 0:
    for i in range(60):
        i = list(str(i))
        if '3' in i:
            cnt += 60
            continue
        for j in range(60):
            j = list(str(j))
            if '3' in j:
                cnt += 1
                continue
else:
    for i in range(n+1):
        i = list(str(i))
        if '3' in i:
            cnt += 60 * 60
            continue
        for j in range(60):
            j = list(str(j))
            if '3' in j:
                cnt += 60
                continue
            for k in range(60):
                k = list(str(k))
                if '3' in k:
                    cnt += 1
                    continue
print(cnt)