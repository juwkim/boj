g = lambda: [*map(int, input().split())]
import heapq
def dijkstra(graph, i, j):
    distances = [[float('inf')] * len(graph[0]) for _ in range(len(graph))]
    distances[i][j] = graph[i][j]

    heap = []
    heapq.heappush(heap, (graph[i][j], i, j))
    while heap:
        current_distance, x, y = heapq.heappop(heap)
        for a, b in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)):
            if 0 <= a < len(graph) and 0 <= b < len(graph[0]):
                if current_distance + graph[a][b] < distances[a][b]:
                    distances[a][b] = current_distance + graph[a][b]
                    heapq.heappush(heap, (distances[a][b], a, b))
    return distances

step = 1
while N:= int(input()):
    graph = [g() for _ in range(N)]
    ans = dijkstra(graph, 0, 0)[-1][-1]
    print(f'Problem {step}: {ans}')
    step += 1