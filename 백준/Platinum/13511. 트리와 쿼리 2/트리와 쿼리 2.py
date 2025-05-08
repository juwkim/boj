import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

LOG = 17
N = int(input())
tree = [[] for _ in range(N + 1)]

for _ in range(N - 1):
    u, v, w = map(int, input().split())
    tree[u].append((v, w))
    tree[v].append((u, w))

depth = [0] * (N + 1)
up = [[-1] * LOG for _ in range(N + 1)]
dist = [[0] * LOG for _ in range(N + 1)]

def dfs(node, parent):
    for nxt, weight in tree[node]:
        if nxt != parent:
            depth[nxt] = depth[node] + 1
            up[nxt][0] = node
            dist[nxt][0] = weight
            for i in range(1, LOG):
                if up[nxt][i - 1] != -1:
                    up[nxt][i] = up[up[nxt][i - 1]][i - 1]
                    dist[nxt][i] = dist[nxt][i - 1] + dist[up[nxt][i - 1]][i - 1]
            dfs(nxt, node)

dfs(1, -1)

def get_dist(u, v):
    total = 0
    if depth[u] < depth[v]:
        u, v = v, u

    for i in range(LOG - 1, -1, -1):
        if depth[u] - (1 << i) >= depth[v]:
            total += dist[u][i]
            u = up[u][i]

    if u == v:
        return total

    for i in range(LOG - 1, -1, -1):
        if up[u][i] != -1 and up[u][i] != up[v][i]:
            total += dist[u][i] + dist[v][i]
            u = up[u][i]
            v = up[v][i]

    total += dist[u][0] + dist[v][0]
    return total

def lca(u, v):
    if depth[u] < depth[v]:
        u, v = v, u

    for i in range(LOG - 1, -1, -1):
        if depth[u] - (1 << i) >= depth[v]:
            u = up[u][i]

    if u == v:
        return u

    for i in range(LOG - 1, -1, -1):
        if up[u][i] != -1 and up[u][i] != up[v][i]:
            u = up[u][i]
            v = up[v][i]

    return up[u][0]

def kth_node(u, v, k):
    l = lca(u, v)
    if k > depth[u] - depth[l] + 1:
        return kth_ancestor(v, depth[v] - depth[l] - (k - depth[u] + depth[l] - 1))
    return kth_ancestor(u, k - 1)

def kth_ancestor(node, k):
    for i in range(LOG - 1, -1, -1):
        if k & (1 << i):
            node = up[node][i]
    return node    

for _ in range(int(input())):
    cmd, u, v, *k = map(int, input().split())
    if cmd == 1:
        print(get_dist(u, v))
    else:
        print(kth_node(u, v, k[0]))