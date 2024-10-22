n, *a, k = map(int, open(0).read().split())
ans, sum, l, r = 0, 0, 0, 0
while r < n:
    if sum <= k:
        sum += a[r]
        r += 1
    else:
        while sum > k:
            ans += n - r + 1
            sum -= a[l]
            l += 1
while sum > k:
    ans += n - r + 1
    sum -= a[l]
    l += 1
print(ans)