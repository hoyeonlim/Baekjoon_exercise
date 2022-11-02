def d(n):
    a=(n//1000)
    b=((n-1000*a)//100)
    c=((n-1000*a-100*b)//10)
    d=n-1000*a-100*b-10*c
    return (n+a+b+c+d)

num_list = list(range(1,10000))
del_list = []
for i in range (1, 10000):
    if d(i) not in del_list:
        del_list.append(d(i))

self_list = [x for x in num_list if x not in del_list]

for i in self_list:
    print(i)
