import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

LOG = 17  # 2^17 > 100000
N = int(input())
tree = [[] for _ in range(N+1)]
for _ in range(N-1):
    u, v = map(int, input().split())
    tree[u].append(v)
    tree[v].append(u)

depth = [0] * (N+1)
up = [[-1] * (N+1) for _ in range(LOG)]

def dfs(v, p):
    up[0][v] = p
    for i in range(1, LOG):
        if up[i-1][v] != -1:
            up[i][v] = up[i-1][up[i-1][v]]
    for to in tree[v]:
        if to != p:
            depth[to] = depth[v] + 1
            dfs(to, v)

dfs(1, -1)
def lca(u, v):
    if depth[u] < depth[v]:
        u, v = v, u

    for i in range(LOG-1, -1, -1):
        if depth[u] - (1 << i) >= depth[v]:
            u = up[i][u]

    if u == v:
        return u

    for i in range(LOG-1, -1, -1):
        if up[i][u] != -1 and up[i][u] != up[i][v]:
            u = up[i][u]
            v = up[i][v]

    return up[0][u]

for _ in range(int(input())):
    u, v = map(int, input().split())
    print(lca(u, v))