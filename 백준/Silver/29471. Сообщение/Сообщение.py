def sieve(N):
    primes = [False, False] + [True] * (N - 1)
    for i in range(2, int(N**.5) + 1):
        if primes[i] == False:
            continue
        for j in range(i * i, N + 1, i):
            primes[j] = False
    return primes

primes = sieve(10000000)
k = int(input())
p = 2
while True:
    if primes[p] and primes[2 * p + 1]:
        k -= 1
        if k == 0:
            break
    p += 1
print(p)