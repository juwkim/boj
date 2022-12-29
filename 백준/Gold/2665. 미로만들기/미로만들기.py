from collections import deque
def zero_one(graph, i, j):
    distances = [[float('inf')] * len(graph[0]) for _ in range(len(graph))]
    distances[i][j] = graph[i][j]

    dq = deque([(distances[i][j], i, j)])
    while dq:
        current_distance, x, y = dq.popleft()
        for a, b in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)):
            if 0 <= a < len(graph) and 0 <= b < len(graph[0]):
                if current_distance + graph[a][b] < distances[a][b]:
                    distances[a][b] = current_distance + graph[a][b]
                    if graph[a][b]:
                        dq.append((distances[a][b], a, b))
                    else:
                        dq.appendleft((distances[a][b], a, b))
    return distances
g = lambda: [*map(int, input().split())]
N = int(input())
graph = [[*map(lambda c: 1 - int(c), input())] for _ in range(N)]
distances = zero_one(graph, 0, 0)
print(distances[-1][-1])