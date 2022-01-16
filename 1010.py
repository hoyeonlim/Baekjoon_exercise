from sys import stdin

def site(x):
    ans = 1
    for i in range(1, x+1):
        ans = ans * i
    return ans

t = int(stdin.readline())

for i in range (0, t):
    n, m = map(int, stdin.readline().split())
    answer = site(m) // (site(n) * site(m-n))
    print(answer)
