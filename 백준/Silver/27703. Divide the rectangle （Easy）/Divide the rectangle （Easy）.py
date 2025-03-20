import sys
input = sys.stdin.readline
g = lambda: map(int, input().split())

for _ in range(int(input())):
    input()
    r, c = g()
    rr, cr = g()
    rb, cb = g()
    if r & 1 and c & 1:
        print("IMPOSSIBLE")
    elif r % 2 == 0:
        a = [['R'] * c for i in range(r >> 1)]
        for _ in range(r >> 1):
            a.append(['B'] * c)
        if 2 * rr > r:
            a[rr - 1][cr - 1], a[r - rr][cr - 1] = "RB"
        if 2 * rb <= r:
            a[rb - 1][cb - 1], a[r - rb][cb - 1] = "BR"
        for l in a:
            print(*l, sep="")
    else:
        a = [['R'] * (c >> 1) + ['B'] * (c >> 1) for i in range(r)]
        if 2 * cr > c:
            a[rr - 1][cr - 1], a[rr - 1][c - cr] = "RB"
        if 2 * cb <= c:
            a[rb - 1][cb - 1], a[rb - 1][c - cb] = "BR"
        for l in a:
            print(*l, sep="")
    print()