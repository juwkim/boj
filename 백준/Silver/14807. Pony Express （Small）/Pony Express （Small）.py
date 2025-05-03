import sys
import heapq
from math import inf
input = sys.stdin.readline

def dijkstra(N, graph, start):
    dist = [inf] * N
    dist[start] = 0
    hq = [(0, start)]
    while hq:
        d, u = heapq.heappop(hq)
        if d > dist[u]: continue
        for v in range(N):
            if graph[u][v] < inf:
                if dist[v] > dist[u] + graph[u][v]:
                    dist[v] = dist[u] + graph[u][v]
                    heapq.heappush(hq, (dist[v], v))
    return dist

for tc in range(1, int(input()) + 1):
    N, Q = map(int, input().split())
    E, S = zip(*[map(int, input().split()) for _ in range(N)])
    dist = [[(int(x), inf)[x == '-1'] for x in input().split()] for _ in range(N)]
    for i in range(N):
        dist[i][i] = 0

    for k in range(N):
        for i in range(N):
            for j in range(N):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    time = [[inf] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if dist[i][j] <= E[i]:
                time[i][j] = dist[i][j] / S[i]
    table = [dijkstra(N, time, i) for i in range(N)]
    print(f"Case #{tc}:", end='')
    for _ in range(Q):
        u, v = map(int, input().split())
        print(f" {table[u-1][v-1]}", end='')
    print()