input = __import__('sys').stdin.readline
g = lambda: [*map(int, input().split())]

def bellman_ford(graph, source):
    
    distances = [float('inf')] * (N + 1)
    distances[source] = 0
    
    for _ in range(len(graph) - 1):
        updated = False
        for u, v, w in graph:
            if distances[u] + w < distances[v]:
                distances[v] = distances[u] + w
                updated = True
        if updated == False:
            break
    
    for u, v, w in graph:
        if distances[u] + w < distances[v]:
            return False    
    return True

for _ in range(int(input())):
    N, M, W = g()
    graph = []
    for _ in range(M):
        S, E, T = g()
        graph.append((S, E, T))
        graph.append((E, S, T))
    
    end = []
    for _ in range(W):
        S, E, T = g()
        graph.append((S, E, -T))
        end.append(E)

    if any(bellman_ford(graph, source) == False for source in end):
        print('YES')
    else:
        print('NO')