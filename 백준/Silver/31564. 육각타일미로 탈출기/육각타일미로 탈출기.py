import sys
g = lambda: map(int, sys.stdin.readline().split())
from collections import deque

N, M, K = g()
visited = [bytearray(M) for _ in range(N)]
for _ in range(K):
    Y, X = g()
    visited[Y][X] = 1
visited[0][0] = 1
dq = deque([(0, 0, 0)])
ans = -1
while dq:
    y, x, d = dq.popleft()
    if y == N - 1 and x == M - 1:
        ans = d
        break
    if y & 1:
        dd = (-1, 0), (-1, 1), (0, -1), (0, 1), (1, 0), (1, 1)
    else:
        dd = (-1, -1), (-1, 0), (0, -1), (0, 1), (1, -1), (1, 0)
    for dy, dx in dd:
        ny, nx = y + dy, x + dx
        if 0 <= ny < N and 0 <= nx < M and not visited[ny][nx]:
            visited[ny][nx] = 1
            dq.append((ny, nx, d + 1))
print(ans)