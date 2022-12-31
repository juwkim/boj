input = __import__('sys').stdin.readline
g = lambda: [*map(int, input().split())]

def Floyd_Warshall(graph, n):
    for m in range(1, n + 1):
        for s in range(1, n + 1):
            for e in range(1, n + 1):
                graph[s][e] = min(graph[s][e], graph[s][m] + graph[m][e])

n, m, = g()
graph = [[float('inf')] * (n + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    graph[i][i] = 0

for _ in range(m):
    a, b, c = g()
    graph[a][b] = c

Floyd_Warshall(graph, n)
ans = 1e9
for s in range(1, n):
    for e in range(s + 1, n + 1):
        ans = min(ans, graph[s][e] + graph[e][s])
if ans == 1e9:
    ans = -1
print(ans)