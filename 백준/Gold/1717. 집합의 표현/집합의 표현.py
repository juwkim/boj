import sys
input = sys.stdin.readline

n, m = map(int, input().split())
parent = [*range(n + 1)]
rank = [0] * (n + 1)

def find(x):
    p = x
    while p != parent[p]:
        p = parent[p]
    parent[x] = p
    return p

def union(x, y):
    x, y = find(x), find(y)
    if x == y:
        return
    if rank[x] < rank[y]:
        parent[x] = y
    else:
        parent[y] = x
        if rank[x] == rank[y]:
            rank[x] += 1

for _ in range(m):
    op, a, b = map(int, input().split())
    if op:
        print(("NO", "YES")[find(a) == find(b)])
    else:
        union(a, b)