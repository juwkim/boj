n, m = map(int, input().split())
ans = 0
if m % n:
    d = 1 / (n + m)
    l, r = d, 2 * d
    for i in range(1, n + 1):
        pos = i / n
        while l + d < pos: l += d
        while r < pos: r += d
        ans += min(pos - l, r - pos)
    ans *= 10000
print(ans)