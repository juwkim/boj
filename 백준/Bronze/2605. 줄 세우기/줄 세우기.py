n = []
for i, o in enumerate(map(int, [*open(0)][1].split())):
    n.insert(i-o,i+1)
print(*n)