import sys
input = sys.stdin.readline

def sieve(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    primes = []
    for i in range(2, n + 1):
        if is_prime[i]:
            primes.append(i)
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
    return primes

def find(par, x):
    if par[x] != x:
        par[x] = find(par, par[x])
    return par[x]

def union(par, x, y):
    rx = find(par, x)
    ry = find(par, y)
    if rx != ry:
        par[ry] = rx

primes = sieve(1000)
for tc in range(1, 1 + int(input())):
    A, B, P = map(int, input().split())
    n = B - A + 1
    par = list(range(n))
    for p in primes:
        if p < P: 
            continue
        start = ((A + p - 1) // p) * p
        if start + p > B:
            continue
        first_idx = start - A
        for x in range(start + p, B + 1, p):
            union(par, first_idx, x - A)
    roots = set(find(par, i) for i in range(n))
    print(f"Case #{tc}: {len(roots)}")