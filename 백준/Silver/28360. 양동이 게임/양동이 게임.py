import sys
g = lambda: map(int, sys.stdin.readline().split())

N, M = g()
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    u, w = g()
    graph[u].append(w)
water = [0] * (N + 1)
water[1] = 100
for i in range(1, N + 1):
    if not graph[i]:
        continue
    num = water[i] / len(graph[i])
    water[i] = 0
    for j in graph[i]:
        water[j] += num
print(max(water))