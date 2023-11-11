import sys
input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

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

for tc in range(1, 1 + int(input())):
    graph1, graph2 = defaultdict(list), defaultdict(list)
    for _ in range(int(input())):
        after, before = input().split(':')
        graph1[before].append(after)
        graph2[after].append(before)
    visited = set()
    for _ in range(int(input())):
        dq = deque([input()])
        while dq:
            cur = dq.popleft()
            if cur in visited:
                continue
            visited.add(cur)
            for neighbor in graph2[cur]:
                dq.append(neighbor)
    order = {k: i for i, k in enumerate(topological_sort(graph1))}
    ans = sorted(visited, key=lambda x: order.get(x, 0))
    print(f"Case #{tc}: {len(ans)}")
    print('\n'.join(ans))
