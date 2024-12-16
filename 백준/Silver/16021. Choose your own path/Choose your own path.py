import sys
input = sys.stdin.readline
g = lambda: [*map(int, input().split())]
from collections import deque

N = int(input())
graph = [[]]
for _ in range(N):
    graph.append(g()[1:])
dist = [1e9] * (N + 1)
dist[1] = 1
dq = deque([1])
ans = 1e9
while dq:
    cur = dq.popleft()
    if graph[cur]:
        for nxt in graph[cur]:
            if dist[nxt] == 1e9:
                dist[nxt] = dist[cur] + 1
                dq.append(nxt)
    else:
        ans = min(ans, dist[cur])
if all(d != 1e9 for d in dist[2:]):
    print("Y")
else:
    print("N")
print(ans)