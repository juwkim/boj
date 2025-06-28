for n in map(int, open(0)):
    level, cur = 0, 1
    while cur + 6 * level < n:
        cur += 6 * level
        level += 1
    x, y = level, 0
    for dx, dy in (-1, 1), (-1, 0), (0, -1), (1, -1), (1, 0), (0, 1):
        if n == cur:
            break
        step = min(n - cur, level)
        x += dx * step
        y += dy * step
        cur += step
    print(x, y)