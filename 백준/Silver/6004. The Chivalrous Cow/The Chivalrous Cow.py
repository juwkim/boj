import sys
input = sys.stdin.readline
from collections import deque

X, Y = map(int, input().split())
a = [input() for _ in range(Y)]
x, y = -1, -1
for i in range(Y):
    for j in range(X):
        if a[i][j] == 'K':
            y, x = i, j
            break
    else:
        continue
    break
visited = [bytearray(X) for _ in range(Y)]
visited[y][x] = 1
dq = deque([(y, x, 0)])
while dq:
    y, x, d = dq.popleft()
    if a[y][x] == 'H':
        print(d)
        break
    for ny, nx in (y - 2, x - 1), (y - 2, x + 1), (y - 1, x - 2), (y - 1, x + 2), (y + 1, x - 2), (y + 1, x + 2), (y + 2, x - 1), (y + 2, x + 1):
        if 0 <= ny < Y and 0 <= nx < X and a[ny][nx] != '*' and not visited[ny][nx]:
            visited[ny][nx] = 1
            dq.append((ny, nx, d + 1))