def Sieve_of_Eratosthenes(N):
    array = [True for i in range(N+1)]
    for i in range(2, int(N**.5) + 1):
        if array[i]:
            j = 2
            while i * j <= N:
                array[i * j] = False
                j += 1
    primes = [num for num in range(2, N+1) if array[num]]
    return primes

primes = Sieve_of_Eratosthenes(479909)
print(primes[int(input())-1])