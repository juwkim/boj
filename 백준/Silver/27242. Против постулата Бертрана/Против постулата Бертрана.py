import math
from itertools import pairwise

def segmented_primes(a, b):
    limit = int(math.isqrt(b)) + 1
    is_small = [True] * (limit + 1)
    is_small[0], is_small[1] = False, False
    for i in range(2, limit + 1):
        if is_small[i]:
            for j in range(i * i, limit + 1, i):
                is_small[j] = False
    base_primes = [i for i in range(2, limit + 1) if is_small[i]]
    seg_len = b - a + 1
    is_prime = [1] * seg_len
    for p in base_primes:
        start = max(p * p, (a + p - 1) // p * p)
        for m in range(start, b + 1, p):
            is_prime[m - a] = 0
    for x in 0, 1:
        if a <= x <= b:
            is_prime[x - a] = 0
    return [a + i for i, flag in enumerate(is_prime) if flag]

n = int(input())
primes = [n] + segmented_primes(n + 1, 2 * n - 1) + [2 * n]
ans = min((p - q, p + 1, q - 1) for p, q in pairwise(primes))
print(*ans[1:])