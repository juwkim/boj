import sys
input = sys.stdin.readline
g = lambda: [*map(int, input().split())]

while True:
    N, K, M = g()
    if N == 0:
        break
    friends = g()
    graph = [[] for _ in range(N)]
    for _ in range(M):
        a, b = g()
        graph[a - 1].append(b - 1)
    visited = bytearray(N)
    for friend in friends:
        stack = [friend - 1]
        visited[friend - 1] = True
        while stack:
            node = stack.pop()
            for neighbor in graph[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    stack.append(neighbor)
    if all(visited):
        ans = "yes"
    else:
        ans = "no"
    print(ans)