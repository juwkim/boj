g = lambda: [*map(int, input().split())]

H, W = g()
for _ in range(H):
    pos = -1
    buf = []
    for idx, cloud in enumerate(input()):
        if cloud == 'c':
            buf.append(0)
            pos = idx
        elif pos == -1:
            buf.append(-1)
        else:
            buf.append(idx - pos)
    print(*buf)