import sys
from collections import deque
g = lambda: map(int, sys.stdin.readline().split())

N, M = g()
X, Y = g()
ans = [[0] * (N + 1) for _ in range(N + 1)]
visited = [bytearray(N + 1) for _ in range(N + 1)]
visited[X][Y] = 1
dq = deque([(X, Y, 0)])
while dq:
    x, y, c = dq.popleft()
    for dx, dy in ((1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)):
        nx, ny = x + dx, y + dy
        if 0 < nx <= N and 0 < ny <= N and not visited[nx][ny]:            
            visited[nx][ny] = 1
            ans[nx][ny] = c + 1
            dq.append((nx, ny, c + 1))
for _ in range(M):
    x, y = g()
    print(ans[x][y])