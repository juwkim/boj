l = [*open(0)]
idx = 0

def draw(c, x, y):
    if 0 <= x < M and 0 <= y < M:
        a[M - 1 - y][x] = c

while idx < len(l):
    M, N = map(int, l[idx].split())
    a = [['.'] * M for _ in range(M)]
    for line in l[idx + 1:idx + 1 + N]:
        s, x, y = map(int, line.split())
        draw('_', x - 1, y)
        draw('_', x + 1, y)
        if s:
            draw('|', x, y)
            draw('^', x, y + s + 1)
            for h in range(y + 1, y + s + 1):
                draw('/', x - 1, h)
                draw('|', x, h)
                draw('\\', x + 1, h)
        else:
            draw('o', x, y)
    idx += N + 1
    print("*" * (M + 2))
    for line in a:
        print("*" + "".join(line) + "*")
    print("*" * (M + 2))
    print()