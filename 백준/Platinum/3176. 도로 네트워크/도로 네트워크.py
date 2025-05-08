import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

LOG = 17
N = int(input())
tree = [[] for _ in range(N + 1)]

for _ in range(N - 1):
    A, B, C = map(int, input().split())
    tree[A].append((B, C))
    tree[B].append((A, C))

depth = [0] * (N + 1)
up = [[-1] * LOG for _ in range(N + 1)]
MIN = [[1e9] * LOG for _ in range(N + 1)]
MAX = [[-1e9] * LOG for _ in range(N + 1)]

def dfs(node, parent):
    for nxt, weight in tree[node]:
        if nxt != parent:
            depth[nxt] = depth[node] + 1
            up[nxt][0] = node
            MIN[nxt][0] = weight
            MAX[nxt][0] = weight            
            for i in range(1, LOG):
                if up[nxt][i - 1] != -1:
                    up[nxt][i] = up[up[nxt][i - 1]][i - 1]
                    MIN[nxt][i] = min(MIN[nxt][i - 1], MIN[up[nxt][i - 1]][i - 1])
                    MAX[nxt][i] = max(MAX[nxt][i - 1], MAX[up[nxt][i - 1]][i - 1])
            dfs(nxt, node)

dfs(1, -1)

def solve(u, v):
    min_dist, max_dist = 1e9, -1e9
    if depth[u] < depth[v]:
        u, v = v, u

    for i in range(LOG - 1, -1, -1):
        if depth[u] - (1 << i) >= depth[v]:
            min_dist = min(min_dist, MIN[u][i])
            max_dist = max(max_dist, MAX[u][i])
            u = up[u][i]

    if u == v:
        return min_dist, max_dist

    for i in range(LOG - 1, -1, -1):
        if up[u][i] != -1 and up[u][i] != up[v][i]:
            min_dist = min(min_dist, MIN[u][i], MIN[v][i])
            max_dist = max(max_dist, MAX[u][i], MAX[v][i])
            u = up[u][i]
            v = up[v][i]

    min_dist = min(min_dist, MIN[u][0], MIN[v][0])
    max_dist = max(max_dist, MAX[u][0], MAX[v][0])
    return min_dist, max_dist

for _ in range(int(input())):
    u, v = map(int, input().split())
    print(*solve(u, v))