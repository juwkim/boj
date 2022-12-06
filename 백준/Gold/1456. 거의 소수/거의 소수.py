def Sieve_of_Eratosthenes(N):
    array = [False, False] + [True for i in range(N-1)]
    for i in range(2, int(N**.5) + 1):
        if array[i]:
            j = 2
            while i * j <= N:
                array[i * j] = False
                j += 1
    primes = [i for i in range(N+1) if array[i]]
    return primes

A, B = map(int, input().split())
primes = Sieve_of_Eratosthenes(int(B**.5))
count = 0
for prime in primes:
    a, b = 0, 0
    x, y = A, B
    while x > prime:
        x /= prime
        a += 1
    while y >= prime:
        y /= prime
        b += 1
    count += b - a - (A <= prime)
print(count)