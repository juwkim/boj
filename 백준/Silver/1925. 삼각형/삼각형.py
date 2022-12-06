g = lambda: [*map(int, input().split())]

x1, y1 = g()
x2, y2 = g()
x3, y3 = g()
if (x3 - x1) * (y2 - y1) == (x2 - x1) * (y3 - y1):
    print('X')
else:
    p, q, r = sorted([(x1 - x2)**2 + (y1 - y2)**2, (x3 - x2)**2 + (y3 - y2)**2, (x1 - x3)**2 + (y1 - y3)**2])
    tmp = p + q
    if p == q == r:
        print('JungTriangle')
    elif p == q or q == r:
        print(['Jikkak2Triangle', 'Yeahkak2Triangle', 'Dunkak2Triangle'][(tmp > r) - (tmp < r)])
    else:
        print(['JikkakTriangle', 'YeahkakTriangle', 'DunkakTriangle'][(tmp > r) - (tmp < r)])