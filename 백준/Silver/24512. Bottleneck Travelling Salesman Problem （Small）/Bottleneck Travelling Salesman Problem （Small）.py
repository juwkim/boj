import sys
g = lambda: map(int, sys.stdin.readline().split())
from itertools import permutations

N, M = g()
graph = [[0] * (N + 1) for _ in range(N + 1)]
for _ in range(M):
    u, v, c = g()
    graph[u][v] = c
ans, cost = -1, 1e9
for p in permutations(range(1, N + 1)):
    cur = -1
    for i in range(N):
        if graph[p[i - 1]][p[i]] == 0:
            cur = -1
            break
        cur = max(cur, graph[p[i - 1]][p[i]])
    if cur != -1 and cur < cost:
        ans, cost = p, cur
if ans == -1:
    print(-1)
else:
    print(cost)
    print(*ans)