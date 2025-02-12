for l in open(0):
    n, *nums = map(int, l.split())
    print(n, end=' ')
    x, y = 0, 0
    for i in range(n):
        a, b = nums[2 * i], nums[2 * i + 1]
        if i & 1:
            x -= a
            y -= b
        else:
            x += a
            y += b
    for i in range(n):
        print(f"{x:.6f} {y:.6f}", end=' ')
        x = 2 * nums[2 * i] - x
        y = 2 * nums[2 * i + 1] - y
    print()