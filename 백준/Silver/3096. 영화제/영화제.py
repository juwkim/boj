import sys
g = lambda: map(int, sys.stdin.readline().split())

N, M = g()
graph = [set() for _ in range(N + 1)]
for _ in range(M):
    a, b = g()
    graph[a].add(b)
ans = 0
for i in range(1, N):
    for j in range(i + 1, N + 1):
        l = len(graph[i] & graph[j])
        ans += l * (l - 1)
print(ans >> 1)