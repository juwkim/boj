N, K, *x = map(int, open(0).read().split())
x.sort()
lo, hi = 0, (x[-1] - x[0] + K) // (2 * K)
while hi > lo + 1:
    mid = lo + hi >> 1
    cnt, cover = 0, -1e9
    for num in x:
        if num > cover:
            cover = num + 2 * mid
            cnt += 1
            if cnt > K:
                lo = mid
                break
    else:
        hi = mid
print(hi)