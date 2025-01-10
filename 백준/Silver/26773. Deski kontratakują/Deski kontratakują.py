N, *L = map(int, open(0).read().split())
L.sort()
lo, hi = 0, L[-1] + 1
while hi > lo + 1:
    mid = lo + hi >> 1
    cnt = sum(l // mid for l in L)
    if cnt >= 4:
        lo = mid
    else:
        hi = mid
print(lo ** 2)