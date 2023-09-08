import sys
input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

from itertools import combinations

N, K = g()
homes = [g() for _ in range(N)]
dist = [[0] * N for _ in range(N)]
for i in range(N):
    for j in range(i):
        p = abs(homes[i][0] - homes[j][0]) + abs(homes[i][1] - homes[j][1])
        dist[i][j], dist[j][i] = p, p

ans = float("inf")
for l in combinations(range(N), K):
    ans = min(ans, max(min(dist[i][j] for j in l) for i in range(N)))
print(ans)