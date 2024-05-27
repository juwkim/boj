import sys
input = sys.stdin.readline
g = lambda: [*map(int, input().split())]

def solve():
    N = int(input())
    graph = [set() for _ in range(N + 1)]
    for _ in range(N - 1):
        a, b = g()
        graph[a].add(b)
        graph[b].add(a)
    path = g()
    if path[0] != 1: return 0
    i = 0
    visited = bytearray(N + 1)
    def dfs():
        nonlocal i
        if i == N - 1: return 1
        visited[v:=path[i]] = 1
        i += 1
        for _ in range(len(graph[v])):
            if path[i] in graph[v] and not visited[path[i]]:
                if dfs(): return 1
        return 0
    return dfs()
print(solve())