for n in map(int, open(0)):
    level, total = 1, 1
    while True:
        next_total = total + 6 * level
        if next_total >= n:
            break
        total = next_total
        level += 1
    idx_in_ring = n - total
    x, y = level - 1, 0
    cnt = 0
    for dx, dy in (0, 1), (-1, 1), (-1, 0), (0, -1), (1, -1), (1, 0), (0, 1):
        if idx_in_ring == 0:
            break
        if cnt == 0:
            step = 1
        elif cnt == 1:
            step = min(idx_in_ring, level - 1)
        else:
            step = min(idx_in_ring, level)
        cnt += 1
        x += dx * step
        y += dy * step
        idx_in_ring -= step
    print(x, y)