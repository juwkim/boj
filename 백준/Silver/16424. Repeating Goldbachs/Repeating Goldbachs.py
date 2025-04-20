def sieve(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
    primes = [i for i, v in enumerate(is_prime) if v]
    return is_prime, primes

x = int(input())
is_prime, primes = sieve(10**6)
cnt = 0
while x >= 4:
    for p in primes:
        if 2 * p > x:
            break
        if is_prime[x - p]:
            x -= 2 * p
            cnt += 1
            break
print(cnt)