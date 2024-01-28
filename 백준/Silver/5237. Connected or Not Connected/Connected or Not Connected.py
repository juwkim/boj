import sys
input = lambda: sys.stdin.readline().rstrip()

for _ in range(int(input())):
    n, k, *l = map(int, input().split())
    graph = [[] for _ in range(n)]
    for i in range(0, 2 * k, 2):
        a, b = l[i], l[i + 1]
        graph[a].append(b)
        graph[b].append(a)
    stack = [0]
    visited = bytearray(n)
    visited[0] = 1
    while stack:
        node = stack.pop()
        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = 1
                stack.append(neighbor)
    if all(visited):
        print('Connected.')
    else:
        print('Not connected.')