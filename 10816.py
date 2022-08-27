from sys import stdin

input = stdin.readline

n = int(input())
a = sorted(list(map(int, input().split())))
m = int(input())
b = list(map(int, input().split()))
# answer = []
num = {}
for k in a:
    if k in num:
        num[k] += 1
    else:
        num[k] = 1
def binary(array, value, left, right):
    if left > right:
        return 0
    mid = (left + right) // 2
    if value == array[mid]:
        return num.get(value)
    if value < array[mid]:
        return binary(a, value, left, mid-1)
    if value > array[mid]:
        return binary(a, value, mid+1, right)

for value in b:
    print(binary(a, value, 0, len(a)-1), end=" ")
# for x in b:
#     if x not in a:
#         answer.append(0)
#         continue
#     answer.append(binary(a, x, 0, len(a)-1))
# print(*answer)