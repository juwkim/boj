g = lambda: [*map(int, input().split())]
from bisect import bisect

N, M, K = g()
A = g()
for B in g():
    idx = bisect(A, B)
    if idx == 0:
        ans = max(0, K - A[0] + B)
    elif idx == N:
        ans = max(0, K - B + A[-1])
    else:
        ans = max(0, K - B + A[idx - 1], K - A[idx] + B)
    print(ans)