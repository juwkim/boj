import sys
input = lambda: sys.stdin.readline().rstrip()

from collections import deque
g = lambda: [*map(int, input().split())]

N, M, V = g()
graph = {i: [] for i in range(1, 1 + N)}

for _ in range(M):
    a, b = g()
    graph[a].append(b)
    graph[b].append(a)
for i in range(1, 1 + N):
    graph[i].sort()


def dfs(node):
    dfs_buf.append(node)
    visited[node] = 1
    for Next in graph[node]:
        if visited[Next] == 0:
            dfs(Next)

def bfs(node):
    qu.append(node)
    bfs_buf.append(node)
    visited[node] = 1

    while qu:
        cur = qu.popleft()
        for Next in graph[cur]:
            if visited[Next] == 0:           
                qu.append(Next)
                visited[Next] = 1
                bfs_buf.append(Next)

qu = deque()
dfs_buf, bfs_buf = [], []
visited = [0 for _ in range(1 + N)]
dfs(V)
visited = [0 for _ in range(1 + N)]
bfs(V)
print(*dfs_buf)
print(*bfs_buf)