n, k, *p = map(int, open(0).read().split())
lo, hi = 0, max(p)
while hi > lo + 1:
    mid = lo + hi >> 1
    if sum((num + mid - 1) // mid for num in p) > k:
        lo = mid
    else:
        hi = mid
print(hi)