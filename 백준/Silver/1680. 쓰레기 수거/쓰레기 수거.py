g = lambda: [*map(int, input().split())]

for _ in range(int(input())):
    W, N = g()
    ans, cur, filled = 0, 0, 0
    for _ in range(N):
        xi, wi = g()
        if filled + wi == W:
            ans += 3 * xi - cur
            filled = 0
        elif filled + wi > W:
            if wi == W:
                ans += 5 * xi - cur
                filled = 0
            else:
                ans += 3 * xi - cur
                filled = wi
        else:
            ans += xi - cur
            filled += wi
        cur = xi
    if filled:
        ans += cur
    else:
        ans -= cur
    print(ans)