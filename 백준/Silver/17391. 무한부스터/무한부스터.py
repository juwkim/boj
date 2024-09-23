import sys
g = lambda: [*map(int, sys.stdin.readline().split())]
from collections import deque

N, M = g()
a = [g() for _ in range(N)]
visited = [bytearray(M) for _ in range(N)]
visited[0][0] = 1
dq = deque([(0, 0, 0)])
while dq:
    x, y, c = dq.popleft()
    if x == N - 1 and y == M - 1:
        print(c)
        break
    for nx in range(x + 1, min(N, x + 1 + a[x][y])):
        if 0 <= nx < N and not visited[nx][y]:
            visited[nx][y] = 1
            dq.append((nx, y, c + 1))
    for ny in range(y + 1, min(M, y + 1 + a[x][y])):
        if 0 <= ny < M and not visited[x][ny]:
            visited[x][ny] = 1
            dq.append((x, ny, c + 1))