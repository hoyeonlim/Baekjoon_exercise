m, n = map(int, input().split())
chess = []
ans = []

for sen in range (0, m):
    chess.append(list(input()))

for i in range (0, m-7):
    for j in range (0, n-7):
        k = 0
        l = 0
        for x in range (i, i+8):
            for y in range (j, j+8):
                if (x + y)%2 == 0:
                    if chess[x][y] != "W":
                        k += 1
                    if chess[x][y] != "B":
                        l += 1
                else:
                    if chess[x][y] != "B":
                        k += 1
                    if chess[x][y] != "W":
                        l += 1
        ans.append(min(k, l))

print(min(ans))