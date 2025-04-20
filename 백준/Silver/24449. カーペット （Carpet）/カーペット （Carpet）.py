import sys
from collections import deque
input = sys.stdin.readline

H, W = map(int, input().split())
grid = [input() for _ in range(H)]
dist = [[-1] * W for _ in range(H)]
dist[0][0] = 0
dq = deque([(0, 0)])
while dq:
    x, y = dq.popleft()
    for nx, ny in (x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1):
        if 0 <= nx < H and 0 <= ny < W:
            if grid[nx][ny] != grid[x][y] and dist[nx][ny] == -1:
                dist[nx][ny] = dist[x][y] + 1
                dq.append((nx, ny))
print(dist[H - 1][W - 1])