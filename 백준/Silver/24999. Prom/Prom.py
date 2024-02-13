g = lambda: map(int, input().split())
from bisect import bisect

n, m, k = g()
A = sorted(g())
ans = sum(bisect(A, B + k) - bisect(A, B - k - 1) for B in sorted(g()))
print(ans)