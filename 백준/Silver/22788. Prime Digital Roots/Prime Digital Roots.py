def sieve(N):
    primes = [False, False] + [True] * (N - 1)
    for i in range(2, int(N**.5) + 1):
        if primes[i] == False:
            continue
        for j in range(i * i, N + 1, i):
            primes[j] = False
    return primes

primes = sieve(1000000)
while N := int(input()):
    num = N
    while num >= 10 and primes[num] == False:
        num = sum(int(i) for i in str(num))
    if primes[num]:
        print(f"{N:7d} {num:7d}")
    else:
        print(f"{N:7d}    none")