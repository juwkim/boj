def g(): return [*map(int, input().split())]

def sieve_of_eratosthenes(N):
    is_prime = [True] * N
    spf = [None] * N
    primes = []
    for i in range(2, N):
        if is_prime[i]:
            primes.append(i)
            spf[i] = i

        for prime in primes:
            if prime > spf[i] or i * prime >= N:
                break
            is_prime[i * prime] = False
            spf[i * prime] = prime

    return primes
                   
from bisect import bisect_left

primes = sieve_of_eratosthenes(1000004)
for _ in range(int(input())):
    ans = sum(primes[bisect_left(primes, num)] for num in g())
    print(ans)