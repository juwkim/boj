import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

def sieve(N):
    is_prime = [False, False] + [True] * (N - 1)
    for i in range(2, int(N**.5) + 1):
        if is_prime[i] == False:
            continue
        for j in range(i * i, N + 1, i):
            is_prime[j] = False
    return [i for i in range(3, N + 1) if is_prime[i]], is_prime

primes, is_prime = sieve(1000000)
while num := int(input()):
    lo, hi = 0, len(primes) - 1
    for prime in primes:
        if is_prime[num - prime]:
            print(f'{num} = {prime} + {num - prime}')
            break