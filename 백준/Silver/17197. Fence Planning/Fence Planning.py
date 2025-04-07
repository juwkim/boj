import sys
g = lambda: [*map(int, sys.stdin.readline().split())]

N, M = g()
x, y = zip(*[g() for _ in range(N)])
parent = [*range(N)]
rank = [0] * N

def find(x):
    while x != parent[x]:
        x = parent[x]
    return x

def union(x, y):
    x, y = find(x), find(y)
    if rank[x] < rank[y]:
        parent[x] = y
    elif rank[x] > rank[y]:
        parent[y] = x
    else:
        parent[y] = x
        rank[x] += 1

for _ in range(M):
    a, b = g()
    union(a - 1, b - 1)

xs = [[1e9, 0] for _ in range(N)]
ys = [[1e9, 0] for _ in range(N)]
for i in range(N):
    p = find(i)
    xs[p][0] = min(xs[p][0], x[i])
    xs[p][1] = max(xs[p][1], x[i])
    ys[p][0] = min(ys[p][0], y[i])
    ys[p][1] = max(ys[p][1], y[i])

ans = float('inf')
for a, b in zip(xs, ys):
    if a[1]:
        ans = min(ans, 2 * (a[1] - a[0] + b[1] - b[0]))
print(ans)