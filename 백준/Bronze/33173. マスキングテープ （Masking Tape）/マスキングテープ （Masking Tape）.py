import sys
g = lambda: map(int, sys.stdin.readline().split())

H, W, Q = g()
color = [[0] * W for _ in range(H)]
mask = [[0] * W for _ in range(H)]
for _ in range(Q):
    q, x, y, *arg = g()
    if q == 1:
        c = arg[0]
        for i in range(x - 1, x + 1):
            for j in range(y - 1, y + 1):
                if not mask[i][j]:
                    color[i][j] = c
    else:
        for i in range(x - 1, x + 1):
            for j in range(y - 1, y + 1):
                mask[i][j] = 1
for l in color:
    print(*l)