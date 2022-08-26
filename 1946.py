from sys import stdin

t = int(stdin.readline())
for i in range(t):
    n = int(stdin.readline())
    arr = [[] for _ in range(n)]
    cnt = 1
    for j in range(n):
        arr[j] = list(map(int, stdin.readline().split()))
    sarr = sorted(arr, key = lambda x : x[0])
    # for k in range(1, t-1):
    #     for l in range(0, k):
    #         ans = sarr[k][1]
    #         if sarr[l][1] < ans:
    #             cnt += 1
    #             break             ### 이중 for문 사용으로 시간초과
    criteria = sarr[0][1]
    for k in range(1, n):
        if sarr[k][1] < criteria:
            cnt += 1
            criteria = sarr[k][1]
    print(cnt)
