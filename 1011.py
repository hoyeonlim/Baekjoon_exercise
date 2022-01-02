def function(k):
    return k*(k+1)
    
n = int(input())

for i in range (0, n):
    x, y = map(int,input().split())
    #초항이 0 등차가 2n인 수열
    k=0
    while True:
        if (y-x) <= function(k):
            if (y - x - function(k-1)) > k:
                k = 2*k
            else:
                k =2*k -1
            break
        k = k + 1
    print(k)
