import sys
input = sys.stdin.readline

N = int(input())
graph = [[]]
for _ in range(N - 1):
    input()
    graph.append([*map(int, input().split())])
graph.append([])
visited = bytearray(N + 1)
def dfs(i):
    for nxt in graph[i]:
        if visited[nxt]:
            return 1
        visited[nxt] = True
        if dfs(nxt):
            return 1
        visited[nxt] = False
    return 0
print(("NO CYCLE", "CYCLE")[dfs(1)])