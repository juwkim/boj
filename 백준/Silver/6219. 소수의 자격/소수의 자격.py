def Sieve_of_Eratosthenes(start, N):
    array = [False, False] + [True for i in range(N-1)]
    for i in range(2, int(N**.5) + 1):
        if array[i]:
            j = 2
            while i * j <= N:
                array[i * j] = False
                j += 1
    primes = [i for i in range(N+1) if array[i] and i >= start]
    return primes

A, B, D = map(int, input().split())
primes = Sieve_of_Eratosthenes(A, B)
print(sum(str(D) in str(prime) for prime in primes))