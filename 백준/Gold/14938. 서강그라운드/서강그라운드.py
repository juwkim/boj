input = __import__('sys').stdin.readline
g = lambda: [*map(int, input().split())]

def Floyd_Warshall(graph, n):
    for m in range(1, n + 1):
        for s in range(1, n + 1):
            for e in range(1, n + 1):
                graph[s][e] = min(graph[s][e], graph[s][m] + graph[m][e])

n, m, r = g()
items = [0] + g()
graph = [[float('inf')] * (n + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    graph[i][i] = 0

for _ in range(r):
    a, b, l = g()
    graph[a][b] = l
    graph[b][a] = l

Floyd_Warshall(graph, n)

ans = 0
for i in range(1, n + 1):
    num = 0
    for j in range(1, n + 1):
        if graph[i][j] <= m:
            num += items[j]
    ans = max(ans, num)
print(ans)