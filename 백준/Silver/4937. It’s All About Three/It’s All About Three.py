for N in [*map(int,open(0))][:-1]:
    ans = "YES"
    cur, d = N, 2
    while d * d <= cur:
        if cur % d == 0:
            if d % 10 != 3:
                ans = "NO"
                break
            cur //= d
        else:
            d += 1
    if cur > 1 and cur % 10 != 3:
        ans = "NO"
    print(N, ans)