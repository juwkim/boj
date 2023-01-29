N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = bytearray(N + 1)

def dfs(node):
    visited[node] = 1
    for Next in graph[node]:
        if visited[Next] == 0:
            dfs(Next)
dfs(1)
ans = [i for i in range(1, N + 1) if visited[i] == 0]
if ans:
    print(*ans)
else:
    print(0)