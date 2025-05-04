def sieve(n):
    is_prime = [True] * (n + 1)
    for i in range(2, int(n ** .5) + 1):
        if is_prime[i]:
            for j in range(i*i, n + 1, i):
                is_prime[j] = False
    return [str(i) for i in range(2, n + 1) if is_prime[i]]

l, h = map(int, input().split())
p = input()
primes = sieve(1299709)
print(sum(p in x for x in primes[l-1:h]))