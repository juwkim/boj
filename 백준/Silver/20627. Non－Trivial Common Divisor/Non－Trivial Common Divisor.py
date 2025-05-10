from collections import Counter
from math import isqrt

N, *A = map(int, open(0))
cnt = Counter()
for a in A:
    for d in range(2, isqrt(a) + 1):
        q, r = divmod(a, d)
        if r == 0:
            cnt[d] += a
            if d != q:
                cnt[q] += a
    if a > 1:
        cnt[a] += a
print(max(cnt.values(), default=0))