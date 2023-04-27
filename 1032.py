from sys import stdin

n = int(stdin.readline())

lst = list(stdin.readline())
lst_len = len(lst)

for i in range(n-1):
    lst2 = list(stdin.readline())
    for j in range(lst_len):
        if lst[j] != lst2[j]:
            lst[j] = '?'

print(''.join(lst))


