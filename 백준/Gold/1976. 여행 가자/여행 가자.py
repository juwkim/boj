import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

N = int(input())
M = int(input())
graph = [g() for _ in range(N)]
parent = [*range(N)]
rank = [0] * N

def find(x):
    if x == parent[x]:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    x = find(x)
    y = find(y)
    if x == y:
        return

    if rank[x] < rank[y]:
        parent[x] = y
    else:
        parent[y] = x
        if rank[x] == rank[y]:
            rank[x] += 1

for i in range(N - 1):
    for j in range(i + 1, N):
        if graph[i][j] == 1:
            union(i, j)

if len(set(find(x-1) for x in g())) == 1:
    print('YES')
else:
    print('NO')