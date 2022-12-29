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

V, E, X = g()
graph = defaultdict(dict)
for _ in range(E):
    u, v, w = g()
    graph[u][v] = w

ans = 0
for start in range(1, V + 1):
    if start != X:
        ans = max(ans, dijkstra(graph, start)[X] + dijkstra(graph, X)[start])
print(ans)