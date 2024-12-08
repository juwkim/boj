import sys
g = lambda: map(int, sys.stdin.readline().split())
from collections import deque

N, M = g()
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    x, y = g()
    graph[x].append(y)
dq = deque([(1, 0)])
visited = bytearray(N + 1)
visited[1] = 1
ans = -1
while dq:
    cur, cnt = dq.popleft()
    if cur == N:
        ans = cnt
        break
    for nxt in graph[cur]:
        if not visited[nxt]:
            visited[nxt] = 1
            dq.append((nxt, cnt + 1))
print(ans)