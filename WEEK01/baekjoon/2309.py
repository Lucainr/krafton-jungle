import sys

dwarf = []

for _ in range(9):
    dwarf.append(int(sys.stdin.readline()))

found = False

for i in range(8):
    for j in range(i+1, 9):
        if sum(dwarf) - dwarf[i] - dwarf[j] == 100:
            real_dwarf = [dwarf[k] for k in range(9) if k != i and k != j]
            found = True
            break
    if found:
        break

real_dwarf.sort()

for tall in real_dwarf:
    print(tall)