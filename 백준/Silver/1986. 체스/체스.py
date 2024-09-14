g = lambda: map(int, input().split())

n, m = g()
a = [[1] * m for _ in range(n)]
q, *queens = g()
k, *knights = g()
p, *pawns = g()
for i in range(0, p * 2, 2):
    x, y = pawns[i] - 1, pawns[i + 1] - 1
    a[x][y] = -1

for i in range(0, q * 2, 2):
    x, y = queens[i] - 1, queens[i + 1] - 1
    a[x][y] = -1

for i in range(0, k * 2, 2):
    x, y = knights[i] - 1, knights[i + 1] - 1
    a[x][y] = -1
    for dx, dy in ((-1, -2), (-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2)):
        if 0 <= x + dx < n and 0 <= y + dy < n and a[x + dx][y + dy] != -1:
            a[x + dx][y + dy] = 0

for i in range(0, q * 2, 2):
    x, y = queens[i] - 1, queens[i + 1] - 1
    for dx, dy in ((-1, -1), (-1, 1), (1, 1), (1, -1), (-1, 0), (0, 1), (1, 0), (0, -1)):
        nx, ny = x + dx, y + dy
        while 0 <= nx < n and 0 <= ny < m and a[nx][ny] != -1:
            a[nx][ny] = 0
            nx += dx
            ny += dy
print(sum(l.count(1) for l in a))