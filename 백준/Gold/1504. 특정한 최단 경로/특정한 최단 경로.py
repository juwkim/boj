input = __import__('sys').stdin.readline
g = lambda: [*map(int, input().split())]

import heapq
def dijkstra(graph, start):
    distances = [float('inf')] * (V + 1)
    distances[start] = 0
    heap = []
    heapq.heappush(heap, (0, start))

    while heap:
        current_distance, current_node = heapq.heappop(heap)
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(heap, (distance, neighbor))
    return distances

from collections import defaultdict

V, E = g()
graph = defaultdict(dict)
for _ in range(E):
    u, v, w = g()
    graph[u][v] = w
    graph[v][u] = w

v1, v2 = g()
a, b, c = dijkstra(graph, 1), dijkstra(graph, v1), dijkstra(graph, v2)
ans = min(a[v1] + b[v2] + c[V], a[v2] + c[v1] + b[V])
if ans == float('inf'):
    print(-1)
else:
    print(ans)