import sys

n = sys.stdin.readline()
alist = set(sys.stdin.readline().split())
m = sys.stdin.readline()
mlist = sys.stdin.readline().split()
print(alist)
for i in mlist:
    sys.stdout.write('1\n') if i in alist else sys.stdout.write('0\n')
