import sys
input = sys.stdin.readline
g = lambda: map(int, input().split())
from collections import deque

n, m = g()
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = g()
    graph[a].append(b)
    graph[b].append(a)
for _ in range(int(input())):
    a, b = g()
    graph[a].append(b)
    graph[b].append(a)
    visited = bytearray(n + 1)
    visited[1] = 1
    dist = [-1] * (n + 1)
    dist[1] = 0
    dq = deque([(1, 0)])
    while dq:
        x, d = dq.popleft()
        for y in graph[x]:
            if not visited[y]:
                visited[y] = 1
                dist[y] = d + 1
                dq.append((y, d + 1))
    print(*dist[1:])