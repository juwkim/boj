import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

LOG = 17
n = int(input())
energy = [int(input()) for _ in range(n)]
tree = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    a, b, c = map(int, input().split())
    tree[a].append((b, c))
    tree[b].append((a, c))

depth = [0] * (n + 1)
up = [[-1] * LOG for _ in range(n + 1)]
dist = [[0] * LOG for _ in range(n + 1)]

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

def solve(u, energy):
    for i in range(LOG - 1, -1, -1):
        if depth[u] - (1 << i) >= 0 and energy >= dist[u][i]:
            energy -= dist[u][i]
            u = up[u][i]
    return u

for i in range(1, n + 1):
    print(solve(i, energy[i - 1]))