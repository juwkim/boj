import sys
input = sys.stdin.readline
g = lambda: [*map(int, input().split())]

dx = -1, -1, -1, 0, 1, 1, 1, 0
dy = -1, 0, 1, 1, 1, 0, -1, -1
jump = [*zip(dx, dy)]
for _ in range(int(input())):
    n, d = g()
    t = n >> 1
    d = (d % 360) // 45
    a = [g() for _ in range(n)]
    for i in range(1, t + 1):
        idx = [(t + i * p, t + i * q) for p, q in jump]
        nums = [a[nx][ny] for nx, ny in idx]
        for j, (nx, ny) in enumerate(idx):
            a[nx][ny] = nums[(j - d) % 8]
    for r in a:
        print(*r)