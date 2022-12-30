from collections import defaultdict, deque

def topological_sort(graph):

    indegree = defaultdict(int)
    for vertex in graph:
        for neighbor in graph[vertex]:
            indegree[neighbor] += 1
    
    sorted_vertices = []
    dq = deque([vertex for vertex in graph if indegree[vertex] == 0])
    while dq:
        vertex = dq.popleft()
        sorted_vertices.append(vertex)

        for neighbor in graph[vertex]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                dq.append(neighbor)

    if len(sorted_vertices) < len(graph):
        return []
    return sorted_vertices

input = __import__('sys').stdin.readline
g = lambda: [*map(int, input().split())]
N, M = g()
graph = {idx: [] for idx in range(1, N + 1)}
for _ in range(M):
    a, b = g()
    graph[a].append(b)

print(*topological_sort(graph))