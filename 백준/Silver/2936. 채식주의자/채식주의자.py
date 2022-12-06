x, y = map(int, input().split())
if x == 0:
    if y < 125:
        t = 250 / (250 - y)
        m, n = 125 * t, (125 - y) * t
    else:
        m, n = 31250 / y, 0
elif y == 0:
    if x < 125:
        t = 250 / (250 - x)
        m, n = (125 - x) * t, 125 * t
    else:
        m, n = 0, 31250 / x
elif y > 125:
    m, n = 250 * (1 - 125 / y), 0
else:
    m, n = 0, 250 * (1 - 125 / x)
print(f'{m:#.2f} {n:#.2f}')