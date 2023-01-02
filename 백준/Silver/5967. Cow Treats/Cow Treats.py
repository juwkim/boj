def g(): return [*map(int, input().split())]


def swap(a, b, is_col):
    if is_col:
        for i in range(H):
            mat[i][a], mat[i][b] = mat[i][b], mat[i][a]
    else:
        for i in range(W):
            mat[a][i], mat[b][i] = mat[b][i], mat[a][i]


W, H = g()
mat = [g() for _ in range(H)]
visited = [bytearray(W) for _ in range(H)]
lim_x, lim_y = -1, -1

while True:

    Max, x, y = 0, None, None
    for i in range(H):
        for j in range(W):
            if visited[i][j] == False and Max < mat[i][j]:
                Max = mat[i][j]
                x, y = i, j

    if Max == 0:
        break

    while x > lim_x + 1:
        swap(x, x - 1, False)
        x -= 1

    while y > lim_y + 1:
        swap(y, y - 1, True)
        y -= 1

    visited[x][y] = True
    lim_x = max(lim_x, x)
    lim_y = max(lim_y, y)

for line in mat:
    print(*line)