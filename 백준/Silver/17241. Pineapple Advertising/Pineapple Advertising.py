import sys
input = sys.stdin.readline
g = lambda: map(int, input().split())

N, M, Q = g()
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    u, v = g()
    graph[u].append(v)
    graph[v].append(u)
visited = bytearray(N + 1)
for _ in range(Q):
    n = int(input())
    cnt = +(not visited[n])
    visited[n] = 1
    for neighbour in graph[n]:
        if not visited[neighbour]:
            visited[neighbour] = 1
            cnt += 1
    graph[n] = []
    print(cnt)