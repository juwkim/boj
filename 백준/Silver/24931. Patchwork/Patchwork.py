g = lambda: [*map(int, input().split())]

R, C = g()
Map = [['.' for _ in range(C)] for _ in range(R)]

patches = []
for _ in range(int(input())):
    a, b = g()
    patch = [input() for _ in range(a)]
    patches.append(patch)

for _ in range(int(input())):
    q, t, p = g()
    patch = patches[p-1]
    
    l = len(patch[0])
    for i in range(q, min(q + len(patch), R)):
        for j in range(t, min(t+l, C)):
            Map[i][j] = patch[i-q][j-t]
for line in Map:
    print(*line, sep='')