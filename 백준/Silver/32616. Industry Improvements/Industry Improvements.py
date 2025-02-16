n, k, *x = map(int, open(0).read().split())
m = max(x)
lo, hi = m - 1, (n + k - 1) // k * m
while hi > lo + 1:
    mid = lo + hi >> 1
    cnt, cur = 1, 0
    for num in x:
        if cur + num <= mid:
            cur += num
        else:
            cnt += 1
            if cnt > k:
                break
            cur = num
    if cnt <= k:
        hi = mid
    else:
        lo = mid
print(hi)