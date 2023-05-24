for _ in range(int(input())):

    ans = (0, 0)
    x, y = 0, 0
    while True:
        p, q = map(int, input().split())
        if (p, q) == (0, 0):
            break
        x, y = x + p, y + q
        ans = max(ans, (x, y), key=lambda t: (t[0]**2 + t[1]**2, t[0]))
    print(*ans)