N, M = map(int, input().split())
a = [bytearray(N + 1) for _ in range(N + 1)]
for _ in range(M):
    p, r, c = input().split()
    r, c = int(r), int(c)
    if p == 'Q':
        for dx, dy in (-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1):
            x, y = r, c
            while 1 <= x <= N and 1 <= y <= N:
                a[x][y] = 1
                x += dx
                y += dy
    elif p == 'R':
        for i in range(1, N + 1):
            a[r][i] = 1
        for i in range(1, N + 1):
            a[i][c] = 1
    else:
        a[r][c] = 1
        for dx, dy in (-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1):
            x, y = r + dx, c + dy
            if 1 <= x <= N and 1 <= y <= N:
                a[x][y] = 1
print(sum(sum(l) for l in a[1:]))