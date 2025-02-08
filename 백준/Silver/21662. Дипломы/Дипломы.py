w, h, n = map(int, input().split())
lo, hi = 0, max(w, h) * (1 + int((n - 1) ** .5))
while lo + 1 < hi:
    mid = (lo + hi) // 2
    cnt = (mid // w) * (mid // h)
    if cnt >= n:
        hi = mid
    else:
        lo = mid
print(hi)