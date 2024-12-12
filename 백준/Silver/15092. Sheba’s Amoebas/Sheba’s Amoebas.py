import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
a = [input() for _ in range(n)]
ans = 0
visited = [bytearray(m) for _ in range(n)]
for i in range(n):
    for j in range(m):
        if a[i][j] != '#' or visited[i][j]:
            continue
        ans += 1
        visited[i][j] = 1
        dq = deque([(i, j)])
        while dq:
            x, y = dq.popleft()
            for dx, dy in (-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1):
                nx, ny = x + dx, y + dy
                if nx < 0 or nx >= n or ny < 0 or ny >= m or visited[nx][ny] or a[nx][ny] == '.':
                    continue
                visited[nx][ny] = 1
                dq.append((nx, ny))
print(ans)