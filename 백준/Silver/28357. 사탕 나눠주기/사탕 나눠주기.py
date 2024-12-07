N, K, *A = map(int, open(0).read().split())

A.sort()
lo, hi = -1, 10**12
while lo + 1 < hi:
    mid = (lo + hi) // 2
    cnt = 0
    for i in range(N - 1, -1, -1):
        if A[i] <= mid or cnt > K:
            break
        cnt += A[i] - mid
    if cnt > K:
        lo = mid
    else:
        hi = mid
print(hi)