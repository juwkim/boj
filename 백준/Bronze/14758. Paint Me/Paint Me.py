g = lambda: [*map(int, input().split())]

while (s := input()) != '0 0 0 0 0 0':
    n, w, l, h, a, m = map(int, s.split())
    ans = w * l + 2 * (w + l) * h
    for _ in range(m):
        x, y = g()
        ans -= x * y
    print((ans * n + a - 1) // a)