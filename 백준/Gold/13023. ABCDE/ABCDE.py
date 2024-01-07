import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

N, M = g()
graph = [[] for _ in range(N)]
for _ in range(M):
    a, b = g()
    graph[a].append(b)
    graph[b].append(a)
ans = 0
def dfs(x, visited):
    global ans
    if len(visited) == 5:
        ans = 1
        return 1
    for nx in graph[x]:
        if nx in visited:
            continue
        dfs(nx, visited + [nx])
for i in range(N):
    dfs(i, [i])
    if ans:
        break
print(ans)