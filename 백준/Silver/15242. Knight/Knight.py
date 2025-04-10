from collections import deque

(x, y), (x1, y1) = map(lambda s: (ord(s[0]) - 97, int(s[1]) - 1), open(0))
dq = deque([(x, y, 0)])
visited = [bytearray(8) for _ in range(8)]
visited[x][y] = 1
while dq:
    x, y, d = dq.popleft()
    if (x, y) == (x1, y1):
        print(d)
        break
    for dx, dy in zip((1, 2, 2, 1, -1, -2, -2, -1), (2, 1, -1, -2, -2, -1, 1, 2)):
        nx, ny = x + dx, y + dy
        if 0 <= nx < 8 and 0 <= ny < 8 and not visited[nx][ny]:
            visited[nx][ny] = 1
            dq.append((nx, ny, d + 1))