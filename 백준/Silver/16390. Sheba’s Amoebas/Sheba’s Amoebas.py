import sys
input = sys.stdin.readline
from collections import deque

m, n = map(int, input().split())
a = [input() for _ in range(m)]
ans = 0
visited = [bytearray(n) for _ in range(m)]
for i in range(m):
    for j in range(n):
        if a[i][j] == '.' or visited[i][j]:
            continue
        ans += 1
        visited[i][j] = 1
        dq = deque([(i, j)])
        while dq:
            x, y = dq.popleft()
            for nx, ny in (x - 1, y - 1), (x - 1, y), (x - 1, y + 1), (x, y - 1), (x, y + 1), (x + 1, y - 1), (x + 1, y), (x + 1, y + 1):
                if 0 <= nx < m and 0 <= ny < n and a[nx][ny] == '#' and not visited[nx][ny]:
                    visited[nx][ny] = 1
                    dq.append((nx, ny))
print(ans)