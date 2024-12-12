import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
a = [input() for _ in range(n)]
visited = [bytearray(n) for _ in range(n)]
ans = 0
for i in range(n):
    for j in range(n):
        if a[i][j] == '.' or visited[i][j]:
            continue
        ans += 1
        visited[i][j] = 1
        dq = deque([(i, j)])
        while dq:
            x, y = dq.popleft()
            for nx, ny in (x+1, y), (x-1, y), (x, y+1), (x, y-1):
                if 0 <= nx < n and 0 <= ny < n and a[nx][ny] == '*' and not visited[nx][ny]:
                    visited[nx][ny] = 1
                    dq.append((nx, ny))
print(ans)