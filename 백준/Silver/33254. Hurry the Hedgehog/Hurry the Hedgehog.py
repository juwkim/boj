import sys
g = lambda: map(int, sys.stdin.readline().split())
from collections import deque

n, m, s = g()
is_mush = bytearray(n + 1)
is_mush[1], is_mush[n] = True, True
for x in g():
    is_mush[x] = True
adj = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v = g()
    if is_mush[u] and is_mush[v]:
        adj[u].append(v)
        adj[v].append(u)
dist = [-1] * (n + 1)
dist[1] = 0
dq = deque([1])
while dq:
    u = dq.popleft()
    if u == n:
        break
    for w in adj[u]:
        if dist[w] == -1:
            dist[w] = dist[u] + 1
            dq.append(w)
print(dist[n] + 1)