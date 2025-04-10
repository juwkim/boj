from collections import deque

R, C = map(int, input().split())
grid = [list(input()) for _ in range(R)]

for i in range(R):
    for j in range(C):
        if grid[i][j] == 'C': sx, sy = i, j
        if grid[i][j] == 'B': ex, ey = i, j

v = [bytearray(C) for _ in range(R)]
dq = deque([(sx, sy, 0)])
v[sx][sy] = 1
while dq:
    x, y, d = dq.popleft()
    if (x, y) == (ex, ey):
        print(d)
        break
    for dx, dy in (1, 0), (-1, 0), (0, 1), (0, -1):
        nx, ny = x + dx, y + dy
        if 0 <= nx < R and 0 <= ny < C and not v[nx][ny] and grid[nx][ny] in '.B':
            v[nx][ny] = 1
            dq.append((nx, ny, d + 1))