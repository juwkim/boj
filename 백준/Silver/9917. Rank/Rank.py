import sys
g = lambda: map(int, sys.stdin.readline().split())

N, K = g()
graph = [[] for _ in range(N + 1)]
for _ in range(K):
    a, b, sa, sb = g()
    if sa > sb:
        graph[a].append(b)
    else:
        graph[b].append(a)
def solve(start, node):
    for neighbor in graph[node]:
        if neighbor == start:
            check.update(path)
        elif not visited[neighbor]:
            path.append(neighbor)
            visited[neighbor] = True
            solve(start, neighbor)
            path.pop()
            visited[neighbor] = False
check = set()
visited = bytearray(N + 1)
path = []
for i in range(1, N + 1):
    if graph[i]:
        path.append(i)
        visited[i] = True
        solve(i, i)
        path.pop()
        visited[i] = False
print(len(check))