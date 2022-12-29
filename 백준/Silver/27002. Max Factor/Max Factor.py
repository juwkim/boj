def sieve_of_eratosthenes(N):
    isprime = [True] * N
    spf = [None] * N
    primes = []
    for i in range(2, N):
        if isprime[i]:
            primes.append(i)
            spf[i] = i

        j = 0
        while (j < len(primes) and
              i * primes[j] < N and
              primes[j] <= spf[i]):
         
            isprime[i * primes[j]] = False
            spf[i * primes[j]] = primes[j]
            j += 1
    return primes


def factorization(num):
    factors = []
    cur, p_idx = num, 0
    while primes[p_idx] * primes[p_idx] <= num:
        q, r = divmod(cur, primes[p_idx])
        if r:
            p_idx += 1
        else:
            factors.append(primes[p_idx])
            cur = q
    if not factors or cur != 1:
        factors.append(cur)
    return factors


primes = sieve_of_eratosthenes(1000)
ans = None
max_factor = 0
for _ in range(int(input())):
    N = int(input())
    factor = max(factorization(N))
    if factor > max_factor:
        max_factor = factor
        ans = N
print(ans)