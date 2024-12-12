import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
a = [input() for _ in range(n)]
dist = [[1e9] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if a[i][j] == '0':
            continue
        dq = deque([(i, j)])
        dist[i][j] = 0
        while dq:
            x, y = dq.popleft()
            for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nx, ny = x + dx, y + dy
                if nx < 0 or nx >= n or ny < 0 or ny >= m or a[nx][ny] == '1' or dist[nx][ny] <= dist[x][y] + 1:
                    continue
                dist[nx][ny] = dist[x][y] + 1
                dq.append((nx, ny))
for l in dist:
    print(*l)