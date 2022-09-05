a = [1,2,3]
b= []
b = a.copy()
b.clear()
a.remove(1)
b=a.copy()
print(b, a, sep='\n')