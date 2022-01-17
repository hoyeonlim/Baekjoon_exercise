import sys

def push(x):
    return queue.append(x)
def pop():
    if len(queue) == 0:
        return print(-1)
    else:
        x = queue[0]
        queue.pop(0)
        return print(x)
def size():
    return print(len(queue))
def empty():
    if len(queue) == 0:
        return print(1)
    else:
        return print(0)
def front():
    if len(queue) == 0:
        return print(-1)
    else:
        return print(queue[0])
def back():
    if len(queue) == 0:
        return print(-1)
    else:
        return print(queue[-1])

n = int(sys.stdin.readline())
queue = []
for i in range (0, n):
    func = list(sys.stdin.readline().split())
    if func[0] == "push":
        x = func[1]
        push(x)
        continue
    if func[0] == "pop":
        pop()
        continue
    if func[0] == "size":
        size()
        continue
    if func[0] == "empty":
        empty()
        continue
    if func[0] == "front":
        front()
        continue
    if func[0] == "back":
        back()
        continue