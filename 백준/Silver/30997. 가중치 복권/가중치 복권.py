import sys
g = lambda: map(int, sys.stdin.readline().split())
from itertools import combinations
import math

N, M, K = g()
cnt = [0] * (N + 1)
for _ in range(M - 1):
    for num in g():
        cnt[num] += 1
nums = -1, -1, -1, -1
q = (3 * M)**(K + 1)
for a, b, c in combinations(range(1, N + 1), 3):
    num = cnt[a] + cnt[b] + cnt[c] + 3
    nums = max(nums, ((3 * M - num)**K * num, a, b, c))
p, a, b, c = nums
g = math.gcd(p, q)
print(p // g, q // g)
print(a, b, c)