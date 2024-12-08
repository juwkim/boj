import sys
input = sys.stdin.readline
g = lambda: map(int, input().split())

n, m, Q = g()
a = [bytearray(m + 1) for _ in range(n + 1)]
cnt = n * m
for _ in range(Q):
    cmd, *args = g()
    match cmd:
        case 1:
            dy, dx, y, x = args
            while 1 <= y <= n and 1 <= x <= m and a[y][x] == 0:
                a[y][x] = 1
                cnt -= 1
                y += dy
                x += dx
        case 2:
            y, x = args
            print(a[y][x])
        case 3:
            print(cnt)