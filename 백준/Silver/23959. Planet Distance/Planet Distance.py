from collections import deque

for tc in range(1, int(input()) + 1):
    N = int(input())
    graph = [[] for _ in range(N + 1)]
    for _ in range(N):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    visited = bytearray(N + 1)
    parent = [-1] * (N + 1)
    cycle = []
    def dfs(node, prev):
        for neighbor in graph[node]:
            if neighbor == prev:
                continue
            if visited[neighbor]:
                cur = node
                while cur != neighbor:
                    cycle.append(cur)
                    cur = parent[cur]
                cycle.append(neighbor)
                return True
            else:
                parent[neighbor] = node
                visited[neighbor] = True
                if dfs(neighbor, node):
                    return True
                visited[neighbor] = False
        return False

    visited[1] = True
    dfs(1, -1)
    in_cycle = bytearray(N + 1)
    for x in cycle:
        in_cycle[x] = True

    dist = [-1] * (N + 1)
    dq = deque()
    for i in range(1, N + 1):
        if in_cycle[i]:
            dist[i] = 0
            dq.append(i)
    while dq:
        cur = dq.popleft()
        for neighbor in graph[cur]:
            if dist[neighbor] == -1:
                dist[neighbor] = dist[cur] + 1
                dq.append(neighbor)
    print(f"Case #{tc}:", *dist[1:])