import sys
input = sys.stdin.readline

for tc in range(1, int(input()) + 1):
    N = int(input())
    graph = [[] for _ in range(N + 1)]
    graph[1] = [2, 3]
    graph[2] = [1, 3]
    graph[3] = [1, 2]
    for i in range(4, N + 1):
        a, b = map(int, input().split())
        graph[a].append(i)
        graph[b].append(i)
        graph[i] = [a, b]
    ans = 0
    visited = bytearray(N + 1)
    def dfs(start, node, length):
        global ans
        for neighbor in graph[node]:
            if neighbor == start:
                ans = max(ans, length)
            elif not visited[neighbor]:
                visited[neighbor] = 1
                dfs(start, neighbor, length + 1)
                visited[neighbor] = 0
    for i in range(1, N + 1):
        visited[i] = 1
        dfs(i, i, 1)
        visited[i] = 0
    print(f"Case #{tc}: {ans}")