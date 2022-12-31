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

n, m = g()
graph = [[float('inf')] * (n + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    graph[i][i] = 0

for _ in range(m):
    a, b, c = g()
    graph[a][b] = c
    graph[b][a] = c

path  = [[[s, e] for e in range(n + 1)] for s in range(n + 1)]
Floyd_Warshall(graph, n)

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == j:
            c = '-'
        else:
            c = path[i][j][1]
        print(c, end=' ')
    print()