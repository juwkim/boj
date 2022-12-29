import heapq
def dijkstra(graph, start):
    distances = [float('inf')] * (len(graph) + 1)
    distances[start] = 0
    heap = []
    heapq.heappush(heap, (0, start))
    
    previous = {}
    while heap:
        current_distance, current_node = heapq.heappop(heap)
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(heap, (distance, neighbor))
                previous[neighbor] = current_node
    return distances, previous

g = lambda: [*map(int, input().split())]
V, E = int(input()), int(input())
graph = {node: {} for node in range(1, V + 1)}
for _ in range(E):
    u, v, w = g()
    if v in graph[u]:
        graph[u][v] = min(graph[u][v], w)
    else:
        graph[u][v] = w
start, goal = g()
distances, previous = dijkstra(graph, start)

print(distances[goal])
buf = [goal]
while goal != start:
    buf.append(previous[goal])
    goal = previous[goal]

print(len(buf))
print(*buf[::-1])