x, y = input()
x, y = ord(x) - 97, int(y) - 1
a = [bytearray(8) for _ in range(8)]
dx, dy = (-2, -2, -1, -1, 1, 1, 2, 2), (-1, 1, -2, 2, -2, 2, -1, 1)
for dx1, dy1 in zip(dx, dy):
    nx1, ny1 = x + dx1, y + dy1
    if 0 <= nx1 < 8 and 0 <= ny1 < 8:
        for dx2, dy2 in zip(dx, dy):
            nx2, ny2 = nx1 + dx2, ny1 + dy2
            if 0 <= nx2 < 8 and 0 <= ny2 < 8:
                a[nx2][ny2] = 1
for i in range(8):
    for j in range(8):
        if a[i][j]:
            print(chr(i + 97) + str(j + 1))