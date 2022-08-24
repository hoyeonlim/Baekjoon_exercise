from sys import stdin

pre = stdin.readline().strip()
pre = (' ').join(pre.split('()'))
stack = list(pre)
pieces = 0
lines = 0

while True:
    if stack[-1] == ')':
        lines += 1
        pieces += 1
        stack.pop(-1)
    elif stack[-1] == ' ':
        pieces += lines
        # print("lines =", lines)
        # print("pieces =", pieces)
        stack.pop(-1)
    else:
        lines -= 1
        stack.pop(-1)
    if len(stack) == 0:
        break
print(pieces)
