input = __import__('sys').stdin.readline
g = lambda: [*map(int, input().split())]

def Floyd_Warshall(graph, n):
    for m in range(1, n + 1):
        for s in range(1, n + 1):
            for e in range(1, n + 1):
                dist = graph[s][m] + graph[m][e]
                if dist < graph[s][e]:
                    graph[s][e] = dist
                    path[s][e] = path[s][m] + path[m][e][1:]

n = int(input())
graph = [[float('inf')] * (n + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    graph[i][i] = 0

for _ in range(int(input())):
    a, b, c = g()
    graph[a][b] = min(graph[a][b], c)

path  = [[[s, e] for e in range(n + 1)] for s in range(n + 1)]
Floyd_Warshall(graph, n)

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if graph[i][j] == float('inf'):
            graph[i][j] = 0

for line in graph[1:]:
    print(*line[1:])

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == j or graph[i][j] == 0:
            print(0)
        else:
            print(len(path[i][j]), *path[i][j])