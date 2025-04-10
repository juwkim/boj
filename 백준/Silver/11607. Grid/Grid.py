import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque

n, m = map(int, input().split())
grid = [[*map(int, input())] for _ in range(n)]
visited = [bytearray(m) for _ in range(n)]
dq = deque([(0, 0, 0)])
visited[0][0] = True
while dq:
    x, y, moves = dq.popleft()
    if (x, y) == (n - 1, m - 1):
        print(moves)
        break
    k = grid[x][y]
    if k == 0: continue
    for dx, dy in (-k, 0), (k, 0), (0, -k), (0, k):
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
            visited[nx][ny] = True
            dq.append((nx, ny, moves + 1))
else:
    print("IMPOSSIBLE")