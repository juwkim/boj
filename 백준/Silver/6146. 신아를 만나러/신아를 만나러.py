import sys
g = lambda: map(int, sys.stdin.readline().split())
from collections import deque

X, Y, N = g()
visited = {tuple(g()) for _ in range(N)}
visited.add((0, 0))
dq = deque([(0, 0, 0)])
while dq:
    x, y, cnt = dq.popleft()
    if (x, y) == (X, Y):
        print(cnt)
        break
    for nx, ny in (x-1, y), (x+1, y), (x, y-1), (x, y+1):
        if (nx, ny) not in visited:
            visited.add((nx, ny))
            dq.append((nx, ny, cnt + 1))