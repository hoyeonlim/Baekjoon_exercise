line = str(input())
line2 = line.upper()
cnt = []
up_line = list(set(line.upper()))
for x in up_line:
    cnt.append(line2.count(x))

if cnt.count(max(cnt)) > 1:
    print("?")
else:
    print(up_line[cnt.index(max(cnt))])
