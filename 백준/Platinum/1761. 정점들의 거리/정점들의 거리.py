import sys
sys.setrecursionlimit(50000)
input = sys.stdin.readline

LOG = 16
N = int(input())
tree = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    u, v, d = map(int, input().split())
    tree[u].append((v, d))
    tree[v].append((u, d))

depth = [0] * (N + 1)
up = [[-1] * (N + 1) for _ in range(LOG)]
dist = [[-1] * (N + 1) for _ in range(LOG)]

def dfs(v, p, d):
    up[0][v] = p
    dist[0][v] = d
    for i in range(1, LOG):
        if up[i-1][v] != -1:
            up[i][v] = up[i-1][up[i-1][v]]
            dist[i][v] = dist[i-1][v] + dist[i-1][up[i-1][v]]
    for to, d in tree[v]:
        if to != p:
            depth[to] = depth[v] + 1
            dfs(to, v, d)

dfs(1, -1, -1)
def lca(u, v):
    d = 0
    if depth[u] < depth[v]:
        u, v = v, u

    for i in range(LOG-1, -1, -1):
        if depth[u] - (1 << i) >= depth[v]:
            d += dist[i][u]
            u = up[i][u]

    if u == v:
        return u, d

    for i in range(LOG-1, -1, -1):
        if up[i][u] != -1 and up[i][u] != up[i][v]:
            d += dist[i][u] + dist[i][v]
            u = up[i][u]
            v = up[i][v]

    d += dist[0][u] + dist[0][v]
    return up[0][u], d

for _ in range(int(input())):
    u, v = map(int, input().split())
    lca_node, distance = lca(u, v)
    print(distance)