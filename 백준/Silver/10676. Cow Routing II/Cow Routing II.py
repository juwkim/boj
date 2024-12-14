import sys
g = lambda: [*map(int, sys.stdin.readline().split())]
from collections import defaultdict

A, B, N = g()
d = defaultdict(lambda: 1e9)
for _ in range(N):
    C, T = g()
    nums = g()
    try:
        i = nums.index(A)
        for j in range(i + 1, T):
            d[(A, nums[j])] = min(d[(A, nums[j])], C)
    except:
        pass
    try:
        i = nums.index(B)
        for j in range(i):
            d[(nums[j], B)] = min(d[(nums[j], B)], C)
    except:
        pass
ans = d[(A, B)]
for m in range(1, 10001):
    if m != A and m != B:
        ans = min(ans, d[(A, m)] + d[(m, B)])
print(ans if ans != 1e9 else -1)