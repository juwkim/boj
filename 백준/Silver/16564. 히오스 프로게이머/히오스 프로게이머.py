N, K = map(int, input().split())
X = [int(input()) for _ in range(N)]
lo, hi = min(X) + 1, max(X) + K + 1
while lo + 1 < hi:
    mid = (lo + hi) // 2
    if sum(max(0, mid - x) for x in X) <= K:
        lo = mid
    else:
        hi = mid
print(lo)