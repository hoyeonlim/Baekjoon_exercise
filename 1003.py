import sys
def dp(x):
    arr0 = [1, 0]
    arr1 = [0, 1]
    if x == 0:
        return print(arr0[0], arr1[0], sep=" ")
    elif x == 1:
        return print(arr0[1], ar₩r1[1], sep=" ")
    else:
        for i in range(2, x+1):
            arr0.append(arr0[i-1] + arr0[i-2])
            arr1.append(arr1[i-1] + arr1[i-2])
        return print(arr0[x], arr1[x], sep=" ")

t = int(sys.stdin.readline())
# x == 2 [1, 1]
# x == 3 [1, 2]
# x == 4 [2, 3]
for i in range(0, t):
    a = int(sys.stdin.readline())
    dp(a)
