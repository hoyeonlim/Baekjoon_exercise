import sys
dwarf = [0 for i in range(9)]

for i in range(9):
    dwarf[i] = (int(sys.stdin.readline()))
for j in range(0, 8):
    for k in range(j+1, 9):
        if sum(dwarf) - (dwarf[j] + dwarf[k]) == 100:
            del1 = dwarf[j]
            del2 = dwarf[k]
            break
        else:
            continue
dwarf.remove(del1)
dwarf.remove(del2)
dwarf.sort()

for l in range(0, len(dwarf)):
    print(dwarf[l])
