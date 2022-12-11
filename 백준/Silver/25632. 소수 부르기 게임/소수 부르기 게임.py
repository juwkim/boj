g = lambda: [*map(int, input().split())]

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

primes = sieve_of_eratosthenes(1000)
A, B = g()
yt = set(num for num in primes if A <= num <= B)
C, D = g()
yj = set(num for num in primes if C <= num <= D)

if len(yt) + (len(yt & yj) & 1) > len(yj):
    print('yt')
else:
    print('yj')