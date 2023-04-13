from sys import stdin

input = stdin.readline

n = int(input())
distance = list(map(int, input().split()))
price = list(map(int, input().split()))
tot = distance[0] * price[0]
p = price[0]
for i in range(1, len(distance)):
    if price[i] < p:
        p = price[i]
    tot += distance[i] * p

print(tot)