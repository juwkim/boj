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
start = int(input())
graph = defaultdict(dict)
for _ in range(E):
    u, v, w = g()
    if v in graph[u]:
        graph[u][v] = min(graph[u][v], w)
    else:
        graph[u][v] = w
distance = dijkstra(graph, start)
for idx in range(1, V + 1):
    if distance[idx] == float('inf'):
        print('INF')
    else:
        print(distance[idx])