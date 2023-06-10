g = lambda: [*map(int, input().split())]

for _ in range(int(input())):
    m1, y1 = g()
    m2, y2 = g()
    if y1 == y2:
        ans = 0.5 * (m2 - m1) / (13 - m1)
    else:
        ans = y2 - y1 - 1 + 0.5 + (m2 - 1) / 12
    print("%.4f" % ans)