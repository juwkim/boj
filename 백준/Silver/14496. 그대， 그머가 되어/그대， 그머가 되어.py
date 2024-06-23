import sys
input = sys.stdin.readline
g = lambda: map(int, input().split())
from collections import deque

a, b = g()
N, M = g()
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    s, t = g()
    graph[s].append(t)
    graph[t].append(s)

dq = deque([(a, 0)])
visited = bytearray(N + 1)
visited[a] = 1
ans = -1
while dq:
    x, cnt = dq.popleft()
    if x == b:
        ans = cnt
        break
    for i in graph[x]:
        if not visited[i]:
            visited[i] = 1
            dq.append((i, cnt + 1))
print(ans)