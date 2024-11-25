import sys
input = sys.stdin.readline
from collections import deque

a = [[*map(int, input().split())] for _ in range(5)]
x, y = map(int, input().split())
dq = deque([(x, y, 0)])
visited = [bytearray(5) for _ in range(5)]
visited[x][y] = 1
ans = -1
while dq:
    x, y, cnt = dq.popleft()
    if a[x][y] == 1:
        ans = cnt
        break
    for dx, dy in (0, 1), (0, -1), (1, 0), (-1, 0):
        nx, ny = x + dx, y + dy
        if 0 <= nx < 5 and 0 <= ny < 5 and not visited[nx][ny] and a[nx][ny] != -1:
            visited[nx][ny] = 1
            dq.append((nx, ny, cnt + 1))
print(ans)