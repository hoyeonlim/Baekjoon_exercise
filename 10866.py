import sys
def push_front(x):
    return deque.insert(0, x)
def push_back(x):
    return deque.append( x)
def pop_front():
    if len(deque) == 0:
        return print(-1)
    else:
        first = deque[0]
        deque.pop(0)
        return print(first)
def pop_back():
    if len(deque) == 0:
        return print(-1)
    else:
        last = deque[-1]
        deque.pop(-1)
        return print(last)
def size():
    return print(len(deque))
def empty():
    if len(deque) == 0:
        return print(1)
    else:
        return print(0)
def front():
    if len(deque) == 0:
        return print(-1)
    else:
        return print(deque[0])
def back():
    if len(deque) == 0:
        return print(-1)
    else:
        return print(deque[-1])

n = int(sys.stdin.readline())
deque = []
for i in range (0 ,n):
    sen = list(sys.stdin.readline().split())
    if sen[0] == "push_back":
        push_back(int(sen[1]))
    elif sen[0] == "push_front":
        push_front(int(sen[1]))
    elif sen[0] == "pop_front":
        pop_front()
    elif sen[0] == "pop_back":
        pop_back()
    elif sen[0] == "size":
        size()
    elif sen[0] == "empty":
        empty()
    elif sen[0] == "front":
        front()
    elif sen[0] == "back":
        back()

