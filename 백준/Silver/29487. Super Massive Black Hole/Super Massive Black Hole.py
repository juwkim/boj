n, D, *w = map(int, open(0).read().split())
ans, l, r = 0, D - 1, D + 1
for num in sorted(w, reverse=True)[1:]:
    if l >= 0 and 2 * D < l + r:
        ans += num * (D - l)
        l -= 1
    else:
        ans += num * (r - D)
        r += 1
print(ans)