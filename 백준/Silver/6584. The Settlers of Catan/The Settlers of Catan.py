import sys
g = lambda: [*map(int, sys.stdin.readline().split())]

def dfs(cur, length):
    global ans
    ans = max(ans, length)
    for nxt in graph[cur]:
        a, b = sorted((cur, nxt))
        if not visited[a][b]:
            visited[a][b] = 1
            dfs(nxt, length + 1)
            visited[a][b] = 0

while (l:=g())[0]:
    n, m = l
    graph = [[] for _ in range(n)]
    for _ in range(m):
        u, v = g()
        graph[u].append(v)
        graph[v].append(u)
    ans = 0
    visited = [bytearray(n) for _ in range(n)]
    for start in range(n):
        dfs(start, 0)
    print(ans)