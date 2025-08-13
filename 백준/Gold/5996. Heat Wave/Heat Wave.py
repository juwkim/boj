import sys
g = lambda: map(int, sys.stdin.readline().split())
import heapq

T, C, Ts, Te = g()
adj = [[] for _ in range(T + 1)]
for _ in range(C):
    u, v, w = g()
    adj[u].append((v, w))
    adj[v].append((u, w))

dist = [1e18] * (T + 1)
dist[Ts] = 0
pq = [(0, Ts)]
while pq:
    d, u = heapq.heappop(pq)
    if u == Te:
        break
    for v, w in adj[u]:
        nd = d + w
        if nd < dist[v]:
            dist[v] = nd
            heapq.heappush(pq, (nd, v))
print(dist[Te])