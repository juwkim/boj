import sys
from collections import Counter

def factorize(n):
    factors = Counter()
    for i in range(2, int(n ** 0.5) + 1):
        while n % i == 0:
            factors[i] += 1
            n //= i
    if n > 1:
        factors[n] += 1
    return factors

k = 1
while True:
    A, B = map(int, sys.stdin.readline().split())
    if A == 0:
        break
    p, q = factorize(A), factorize(B)
    X = set(p.keys()) | set(q.keys())
    D = sum(abs(p[x] - q[x]) for x in X)
    ans = 0
    print(f"{k}. {len(X)}:{D}")
    k += 1