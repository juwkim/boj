from math import log2
from collections import Counter

N, *nums = map(int, open(0).read().split())
ans, Min = None, 1e9
for S in range(16):
    for a in range(16):
        for c in range(16):
            cnt = Counter()
            R = S
            for I in nums:
                R = (a * R + c) % 256
                O = (I + R) % 256
                cnt[O] += 1
            H = -sum(cnt[k] * log2(cnt[k] / N) for k in cnt)
            if H < Min:
                Min = H
                ans = (S, a, c)
print(*ans)