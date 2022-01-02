N = int(input())
a = N//5
ans = []
for i in range (a,-1,-1):
    remain = N-5*i
    y = (N-5*i)/3
    if remain%3 != 0:
        continue
    else:
        ans.append(int(i+y))
if len(ans) == 0:
    print(-1)
else:
    print(min(ans))
