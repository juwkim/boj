import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
graph = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    A, B, C = map(int, input().split())
    graph[A].append((B, C))
    graph[B].append((A, C))

dq = deque([(1, 0)])
visited = bytearray(N + 1)
visited[1] = True
ans = 0
while dq:
    node, dist = dq.popleft()
    ans = max(ans, dist)
    for next_node, next_dist in graph[node]:
        if not visited[next_node]:
            visited[next_node] = True
            dq.append((next_node, dist + next_dist))
print(ans)