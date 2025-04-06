import sys
g = lambda: map(int, sys.stdin.readline().split())

N, M = g()
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = g()
    graph[a].append(b)
    graph[b].append(a)
ans, sole = 0, {i for i in range(1, N + 1) if graph[i]}
while len(sole) > 1:
    m = min(len(graph[i]) for i in sole)
    l = [i for i in sole if len(graph[i]) == m]
    p = min(l, key=lambda x: min(len(graph[j]) for j in graph[x]))
    q = min(graph[p], key=lambda x: len(graph[x]))
    ans += 2
    graph[p], graph[q] = [], []
    for i in range(1, N + 1):
        if p in graph[i]:
            graph[i].remove(p)
        if q in graph[i]:
            graph[i].remove(q)
    sole = {i for i in range(1, N + 1) if graph[i]}
if ans < N:
    ans += 1
print(ans)