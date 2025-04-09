import sys
input = sys.stdin.readline
from collections import deque

for _ in range(int(input())):
    m = int(input())
    grid = [input() for _ in range(m)]
    visited = [bytearray(m) for _ in range(m)]
    visited[0][0] = 1
    dq = deque([(0, 0, 0)])
    ans = -1
    while dq:
        x, y, dist = dq.popleft()
        if x == m - 1 and y == m - 1:
            ans = dist
            break
        for dx, dy in (0, 1), (1, 0), (0, -1), (-1, 0):
            nx, ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < m and not visited[nx][ny] and grid[nx][ny] != '*':
                visited[nx][ny] = 1
                dq.append((nx, ny, dist + 1))
    print(ans)