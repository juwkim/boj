input = __import__('sys').stdin.readline
g = lambda: [*map(int, input().split())]
N, M, x, y, K = g()
Map = [g() for _ in range(N)]
dx, dy = [0, 0, 0, -1, 1], [0, 1, -1, 0, 0]
top, btm, front, back, left, right = 0, 0, 0, 0, 0, 0
for cmd in g():
    p, q = x + dx[cmd], y + dy[cmd]
    if 0 <= p < N and 0 <= q < M:
        x, y = p, q
        if cmd == 1:
            top, btm, front, back, left, right = left, right, front, back, btm, top
        elif cmd == 2:
            top, btm, front, back, left, right = right, left, front, back, top, btm
        elif cmd == 3:
            top, btm, front, back, left, right = front, back, btm, top, left, right
        else:
            top, btm, front, back, left, right = back, front, top, btm, left, right

        if Map[x][y]:
            btm = Map[x][y]
            Map[x][y] = 0
        else:
            Map[x][y] = btm
        print(top)