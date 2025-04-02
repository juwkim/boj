n, k, *a = map(int, open(0).read().split())
m = min(a)
lo, hi = m + k // n, m + k + 1
while hi > lo + 1:
    mid = lo + hi >> 1
    if sum(max(0, mid - x) for x in a) > k:
        hi = mid
    else:
        lo = mid
print(lo)