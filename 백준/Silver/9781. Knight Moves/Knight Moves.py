from collections import deque

n, m = map(int, input().split())
grid = [input() for _ in range(n)]

x, y = -1, -1
for i in range(n):
    for j in range(m):
        if grid[i][j] == 'K':
            x, y = i, j
            break
    if x != -1:
        break

visited = [bytearray(m) for _ in range(n)]
dq = deque([(x, y, 0)])
visited[x][y] = True
ans = -1
while dq:
    r, c, d = dq.popleft()
    if grid[r][c] == 'X':
        ans = d
        break
    for dr, dc in (-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1):
        nr, nc = r + dr, c + dc
        if 0 <= nr < n and 0 <= nc < m and not visited[nr][nc] and grid[nr][nc] != '#':
            visited[nr][nc] = True
            dq.append((nr, nc, d + 1))
print(ans)