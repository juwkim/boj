import sys
from collections import deque
g = lambda: map(int, sys.stdin.readline().split())

N, M = g()
S, E = g()
teleport = [[] for _ in range(N + 1)]
for _ in range(M):
    x, y = g()
    teleport[x].append(y)
    teleport[y].append(x)
dq = deque([(S, 0)])
visited = bytearray(N + 1)
visited[S] = 1
while dq:
    x, cnt = dq.popleft()
    if x == E:
        print(cnt)
        break
    for nx in [x - 1, x + 1] + teleport[x]:
        if 1 <= nx <= N and not visited[nx]:
            visited[nx] = 1
            dq.append((nx, cnt + 1))