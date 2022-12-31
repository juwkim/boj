input = __import__('sys').stdin.readline
g = lambda: [*map(int, input().split())]

def Floyd_Warshall(graph, n):
    for m in range(1, n + 1):
        for s in range(1, n + 1):
            for e in range(1, n + 1):
                if graph[s][m] * graph[m][e] > 0:
                    graph[s][e] = graph[s][m]

n, m = int(input()), int(input())
graph = [[0] * (n + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    graph[i][i] = 0

for _ in range(m):
    a, b = g()
    graph[a][b] = 1
    graph[b][a] = -1
Floyd_Warshall(graph, n)
for node in graph[1:]:
    print(node.count(0) - 2)