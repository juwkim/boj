a, b, c, d, e, ans = map(int, open(0))
ans += d + e
a = max(0, a - 11 * e)
if d:
    cnt = min(b, 5 * d)
    b -= cnt; a = max(0, a - 4 * (5 * d - cnt))

ans += (c + 3) // 4; c %= 4
if c:
    cnt = min(b, (0, 5, 3, 1)[c])
    b -= cnt; a = max(0, a - (36 - 9 * c - 4 * cnt))

ans += (b + 8) // 9; b %= 9
if b:
    a = max(0, a - (36 - 4 * b))

ans += (a + 35) // 36
print(ans)