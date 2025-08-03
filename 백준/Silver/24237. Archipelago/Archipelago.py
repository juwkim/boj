import sys
g = lambda: [*map(int, sys.stdin.readline().split())]

n, d = g()
pts = [g() for _ in range(n)]
parent = list(range(n))
rank = [0] * n
def find(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x
def union(a, b):
    ra, rb = find(a), find(b)
    if ra == rb:
        return
    if rank[ra] < rank[rb]:
        parent[ra] = rb
    else:
        parent[rb] = ra
        if rank[ra] == rank[rb]:
            rank[ra] += 1

for i in range(n - 1):
    x1, y1 = pts[i]
    for j in range(i + 1, n):
        if (x1 - pts[j][0])**2 + (y1 - pts[j][1])**2 <= d * d:
            union(i, j)
comp_size = [0] * n
for i in range(n):
    comp_size[find(i)] += 1
print(*sorted(range(1, n + 1), key=lambda i: -comp_size[find(i-1)]))