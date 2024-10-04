import sys
g = lambda: map(int, sys.stdin.readline().split())

N, K = g()
graph = [[float('inf')] * (N + 1) for _ in range(N + 1)]
for i in range(1, N + 1):
    graph[i][i] = 0
for _ in range(K):
    a, b = g()
    graph[a][b] = 1
    graph[b][a] = 1
for k in range(1, N + 1):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
if all(graph[i][j] <= 6 for i in range(1, N) for j in range(i + 1, N + 1)):
    print('Small World!')
else:
    print('Big World!')