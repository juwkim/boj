import sys
sys.setrecursionlimit(10**5)
g = lambda: map(int, sys.stdin.readline().split())

V, E = map(int, input().split())
graph = [[] for _ in range(V + 1)]

for _ in range(E):
    A, B = map(int, input().split())
    graph[A].append(B)

index = 0
dfn = [-1] * (V + 1)
on_stack = [False] * (V + 1)
stack = []
sccs = []

def dfs(u):
    global index
    dfn[u] = index
    index += 1 
    stack.append(u)
    on_stack[u] = True

    parent = dfn[u]
    for v in graph[u]:
        if dfn[v] == -1:
            parent = min(parent, dfs(v))
        elif on_stack[v]:
            parent = min(parent, dfn[v])

    if dfn[u] == parent:
        scc = []
        while True:
            node = stack.pop()
            on_stack[node] = False
            scc.append(node)
            if node == u:
                break
        scc.sort()
        scc.append(-1)
        sccs.append(scc)
    return parent

for u in range(1, V + 1):
    if dfn[u] == -1:
        dfs(u)
print(len(sccs))
for scc in sorted(sccs):
    print(*scc)