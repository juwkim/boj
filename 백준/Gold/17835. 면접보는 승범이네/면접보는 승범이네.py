import heapq
input = __import__('sys').stdin.readline

N, M, K = map(int, input().split())
graph = [{} for _ in range(N + 1)]
for _ in range(M):
    u, v, c = map(int, input().split())
    if u in graph[v]:
        graph[v][u] = min(graph[v][u], c)
    else:
        graph[v][u] = c

heap = []
dist_list = [float('inf')] * (N + 1)
for start in map(int, input().split()):
    dist_list[start] = 0
    heap.append((0, start))
heapq.heapify(heap)

def dijkstra(graph, heap):

    while heap:
        dist, node = heapq.heappop(heap)
        if dist_list[node] < dist:
            continue
        for neighbor, weight in graph[node].items():
            distance = dist + weight
            if distance < dist_list[neighbor]:
                dist_list[neighbor] = distance
                heapq.heappush(heap, (distance, neighbor))

dijkstra(graph, heap)
city = max(range(1, N + 1), key=lambda x: dist_list[x])
print(city)
print(dist_list[city])