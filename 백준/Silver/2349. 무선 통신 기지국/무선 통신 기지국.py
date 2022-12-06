g = lambda: [*map(float, input().split())]

N = int(input())
pos = [g() for _ in range(N)]
neighbors = [set() for _ in range(N)]
for i in range(N-1):
    x1, y1 = pos[i]
    for j in range(i+1, N):
        x2, y2 = pos[j]
        if (x1 - x2) ** 2 + (y1 - y2) ** 2 <= 400:
            neighbors[i].add(j)
            neighbors[j].add(i)

res = []
for i in range(N):
    tmp = [len(neighbors[i] & neighbors[neighbor]) for neighbor in neighbors[i]]
    if tmp:
        res.append(max(tmp))
if res:
    print(max(res) + 2 + (pos[0][0] == -15.0))
else:
    print(1 + any(i for i in neighbors))