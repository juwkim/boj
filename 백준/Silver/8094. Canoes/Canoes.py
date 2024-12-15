w, n, *a = map(int, open(0).read().split())
a.sort()
ans, l, r = 0, 0, n - 1
while l < r:
    if a[l] + a[r] <= w:
        l += 1
    r -= 1
    ans += 1
ans += l == r
print(ans)