import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque

dic = {'N': (-1, 0), 'S': (1, 0), 'E': (0, 1), 'W': (0, -1)}
for tc in range(1, int(input()) + 1):
    x, y, x0, y0, t = map(int, input().split())
    grid = []
    for _ in range(y):
        line = input()
        grid.append([(int(line[j]), dic[line[j + 1]]) for j in range(0, 2 * x, 2)])
    sx, sy = x0 - 1, y0 - 1
    visited = [bytearray(x) for _ in range(y)]
    visited[sy][sx] = True
    dq = deque([(sy, sx)])
    for _ in range(t):
        new = deque()
        while dq:
            cy, cx = dq.popleft()
            s, (dy, dx) = grid[cy][cx]
            for k in range(1, s + 1):
                nx = cx + dx * k
                ny = cy + dy * k
                if 0 <= nx < x and 0 <= ny < y and not visited[ny][nx]:
                    visited[ny][nx] = True
                    new.append((ny, nx))
        dq = new
    print(f"Data Set {tc}:")
    for i in range(y):
        print(*['.X'[visited[i][j]] for j in range(x)], sep='')
    print()