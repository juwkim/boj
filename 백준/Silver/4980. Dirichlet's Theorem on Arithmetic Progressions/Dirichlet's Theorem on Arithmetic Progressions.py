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
            if i * prime >= N or prime > spf[i]:
                break
            is_prime[i * prime] = False
            spf[i * prime] = prime
    return primes
        
primes = set(sieve_of_eratosthenes(1000000))
while sum(l := g()):
    a, d, n = l
    
    cur = a
    while n:
        n -= cur in primes
        cur += d
    print(cur - d)