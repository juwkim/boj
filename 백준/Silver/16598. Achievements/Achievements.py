n, p, *d = map(int, open(0).read().split())
ans, l, r = 0, 0, 0
while r < n:
    num = p - d[r] + d[l] + r - l
    if num < 0:
        l += 1
    else:
        ans = max(ans, d[r] - d[l] + num + 1)
        r += 1
print(ans)