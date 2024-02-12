n, p, *d = map(int, open(0).read().split())
ans, l, r = 0, 0, 0
while r < n:
    if d[r] - d[l] - r + l > p:
        l += 1
    else:
        r += 1
        ans = max(ans, p + r - l)
print(ans)