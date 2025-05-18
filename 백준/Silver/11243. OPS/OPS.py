import sys
input = sys.stdin.readline

def sieve(n):
    is_prime = [False, False] + [True] * (n - 1)
    for i in range(3, int(n ** 0.5) + 1, 2):
        if is_prime[i]:
            for j in range(i*i, n+1, 2*i):
                is_prime[j] = False
    return is_prime

MAX = 1_000_000
is_prime = sieve(MAX)
odd_primes = [i for i in range(3, MAX, 2) if is_prime[i]]

for _ in range(int(input())):
    M = int(input())
    def solve(M):
        for p3 in reversed(odd_primes):
            if p3 > M - 6:
                continue
            rest = M - p3
            for p1 in odd_primes:
                if 2 * p1 > rest:
                    break
                p2 = rest - p1
                if is_prime[p2]:
                    return p3
    print(solve(M))