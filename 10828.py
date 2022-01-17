import sys
def push(x):
    return stack.append(x)

def pop():
    if not stack:
        return print(-1)
    else:
        a = stack[-1]
        stack.pop(-1)
        return print(a)

def size():
    print(len(stack))

def empty():
    if len(stack) == 0:
        print(1)
    else:
        print(0)

def top():
    if len(stack) != 0:
        print(stack[-1])
    else:
        print(-1)

n = int(sys.stdin.readline())
stack = []

for i in range (0, n):
    x = list(sys.stdin.readline().split())
    if x[0] == "push":
        push(int(x[1]))
    elif x[0] == "pop":
        pop()
    elif x[0] == "size":
        size()
    elif x[0] == "empty":
        empty()
    elif x[0] == "top":
        top()
# pop()
# print(stack)
