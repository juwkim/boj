x, y, d = 47, 48, 0
dx, dy = (1, 0, -1, 0), (0, -1, 0, 1)
miro = [['#'] * 97 for _ in range(97)]
miro[x][y] = '.'
xmin, xmax, ymin, ymax = 47, 47, 48, 48
input()
for c in input():
    if c == 'F':
        x, y = x + dx[d], y + dy[d]
        miro[x][y] = '.'
        xmin, xmax, ymin, ymax = min(xmin, x), max(xmax, x), min(ymin, y), max(ymax, y)
    elif c == 'R':
        d = (d + 1) % 4
    else:
        d = (d + 3) % 4
for i in range(xmin, xmax + 1):
    print(*miro[i][ymin:ymax + 1], sep='')