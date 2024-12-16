import sys
input = sys.stdin.readline
from collections import deque

X, Y, Mx, My = map(int, input().split())
a = [input() for _ in range(Y)]
visited = [bytearray(X) for _ in range(Y)]
visited[Y - My][Mx - 1] = 1
ans = 0
dq = deque([(Y - My, Mx - 1, 0)])
while dq:
    y, x, t = dq.popleft()
    ans = max(ans, t)
    for dy, dx in (-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1):
        ny, nx = y + dy, x + dx
        if 0 <= ny < Y and 0 <= nx < X and not visited[ny][nx] and a[ny][nx] == '.':
            visited[ny][nx] = 1
            dq.append((ny, nx, t + 1))
print(ans)