g = lambda: [*map(int, input().split())]

dx = [-2, -2, -1, -1, 1, 1, 2, 2]
dy = [1, -1, 2, -2, 2, -2, 1, -1]
from collections import deque
for _ in range(int(input())):
    l = int(input())
    x, y = g()
    a, b = g()
    dq = deque([(x, y, 0)])
    visited = [bytearray(l) for _ in range(l)]
    visited[x][y] = 1
    while dq:
        x, y, t = dq.popleft()
        if (x, y) == (a, b):
            print(t)
            break
        t += 1
        for p, q in zip(dx, dy):
            u, v = x + p, y + q            
            if 0 <= u < l and 0 <= v < l and visited[u][v] == 0:
                visited[u][v] = 1
                dq.append((u, v, t))