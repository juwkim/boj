import sys
input = lambda: sys.stdin.readline().rstrip()


g = lambda: [*map(int, input().split())]

from collections import deque
def bfs(node):
    qu = deque([node])
    visited[node] = 1

    while qu:
        cur = qu.popleft()
        for Next in graph[cur]:
            if visited[Next] == 0:           
                qu.append(Next)
                visited[Next] = 1


N, M = g()
graph = {i: [] for i in range(1, 1 + N)}
for _ in range(M):
    u, v = g()
    graph[u].append(v)
    graph[v].append(u)

visited = [0 for _ in range(1+N)]

ans = 0
for i in range(1, 1 + N):
    if visited[i] == 0:
        ans += 1
        visited[i] = 1
        bfs(i)
print(ans)