import sys
g = lambda: [*map(int, sys.stdin.readline().split())]
from collections import deque

N, M = g()
Map = [g() for _ in range(M)]
dq = deque([(0, 0)])
visited = [bytearray(N) for _ in range(M)]
ans = "No"
while dq:
    x, y = dq.popleft()
    if x == M - 1 and y == N - 1:
        ans = "Yes"
        break
    for dx, dy in ((0, 1), (1, 0)):
        nx, ny = x + dx, y + dy
        if 0 <= nx < M and 0 <= ny < N and not visited[nx][ny] and Map[nx][ny] == 1:
            visited[nx][ny] = 1
            dq.append((nx, ny))
print(ans)