import sys
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n + 1)]
for _ in range(int(input())):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

ans = -1
visited = bytearray(n + 1)
for i in range(1, n + 1):
    if visited[i]:
        continue
    stack = [i]
    visited[i] = 1
    while stack:
        node = stack.pop()
        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = 1
                stack.append(neighbor)
    ans += 1
print(ans)