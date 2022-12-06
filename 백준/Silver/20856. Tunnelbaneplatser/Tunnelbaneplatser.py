g = lambda: [*map(int, input().split())]


a, b, c, d = g()
ans = d
if c >= a:
    ans += c + (b + 1) // 2
else:
    r, q = divmod(b, 2)
    ans += c + r
    a -= c
    if q:
        ans += 1
        a -= 2
    if a > 0:
        ans += (a + 3) // 4
print(ans)