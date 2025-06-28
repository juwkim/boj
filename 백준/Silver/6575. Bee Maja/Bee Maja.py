for n in map(int, open(0)):
    level, total = 0, 1
    while True:
        next_total = total + 6 * level
        if next_total >= n:
            break
        total = next_total
        level += 1
    idx_in_ring = n - total
    x, y = level, 0
    cnt = 0
    for dx, dy in (-1, 1), (-1, 0), (0, -1), (1, -1), (1, 0), (0, 1):
        if idx_in_ring == 0:
            break
        step = min(idx_in_ring, level)
        cnt += 1
        x += dx * step
        y += dy * step
        idx_in_ring -= step
    print(x, y)