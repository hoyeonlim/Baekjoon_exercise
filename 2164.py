from collections import deque
from sys import stdin

n = int(stdin.readline())
stack = deque()

for i in range(n):
    stack.append(i + 1)

while True:
    if len(stack) == 1:
        break
    stack.popleft()
    stack.append(stack[0])
    stack.popleft()

print(stack.popleft())