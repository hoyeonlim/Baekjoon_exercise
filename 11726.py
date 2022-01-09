# import sys
# def func(x):
#     if x == 1:
#         return 1
#     elif x == 2:
#         return 2
#     else:
#         return func(x-1) + func(x-2)
# n = int(sys.stdin.readline())
#
# print(func(n) % 10007)
n = int(input())

dp = [0 for _ in range(n+1)]

if n <= 3 : print(n)
else :
    dp[1] = 1
    dp[2] = 2
    for i in range(3, n+1):
        dp[i] = dp[i-1] + dp[i-2]

    print(dp[i]%10007)