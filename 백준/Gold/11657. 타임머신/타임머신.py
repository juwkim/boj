import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

N, M = g()
bus = [g() for _ in range(M)]
dist = [float('inf')] * (N + 1)
dist[1] = 0
for i in range(N):
    for u, v, w in bus:
        if dist[u] != float('inf') and dist[v] > dist[u] + w:
            dist[v] = dist[u] + w
            if i == N - 1:
                print(-1)
                exit()
for i in range(2, N + 1):
    print(dist[i] if dist[i] != float('inf') else -1)