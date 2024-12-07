import sys
g = lambda: [*map(int, sys.stdin.readline().split())]
from collections import deque

R, C = g()
A = [g() for _ in range(R)]
visited = [bytearray(C) for _ in range(R)]
ans = 0
for i in range(R):
    for j in range(C):
        if A[i][j] == 0 or visited[i][j]:
            continue
        ans += 1
        dq = deque([(i, j)])
        visited[i][j] = 1
        while dq:
            x, y = dq.popleft()
            for dx, dy in ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)):
                nx, ny = x + dx, y + dy
                if 0 <= nx < R and 0 <= ny < C and not visited[nx][ny] and A[nx][ny]:
                    visited[nx][ny] = 1
                    dq.append((nx, ny))
print(ans)