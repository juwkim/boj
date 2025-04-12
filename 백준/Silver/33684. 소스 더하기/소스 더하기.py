N, K, *A = map(int, open(0).read().split())
A.sort()
if A[-1] > K:
    print(0)
elif A[0] <= 0:
    print(-1)
else:
    cnt, m = 1, 1e18
    for i in range(1, N):
        q = (K - A[i]) // A[0]
        A[i] += q * A[0]
        cnt += q
        m = min(m, A[i])
    cnt += (K - A[0]) // m
    print(cnt)