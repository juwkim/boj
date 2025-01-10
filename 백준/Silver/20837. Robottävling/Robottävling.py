import sys
input = sys.stdin.readline
from collections import Counter
from itertools import product
g = lambda: Counter(map(int, input().split()))

N = int(input())
r, c = g(), g()
Min, cnt = 0, 0
for k in set(r) | set(c):
    cur = max(r[k], c[k])
    cnt += cur
    Min += k * cur
Min += N * N - cnt
Max = sum(v1 * v2 * min(k1, k2) for (k1, v1), (k2, v2) in product(r.items(), c.items()))
print(Min, Max)