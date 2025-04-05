import sys
input = sys.stdin.readline
g = lambda: map(int, input().split())

dx = -1, 0, 1, 0
dy = 0, 1, 0, -1
for _ in range(int(input())):
    n, r = g()
    a = [bytearray(n + 1) for _ in range(n + 1)]
    for _ in range(r):
        x, y = g()
        a[x][y] = 1
    x, y = g()
    if x == n + 1:
        d = 0
    elif y == 0:
        d = 1
    elif x == 0:
        d = 2
    else:
        d = 3
    while True:
        x, y = x + dx[d], y + dy[d]
        if x < 1 or x > n or y < 1 or y > n:
            break
        if a[x][y]:
            d = (d + 1) % 4
    print(x, y)