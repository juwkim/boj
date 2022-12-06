N = int(input())
primes = [num for num in range(2, int(N**0.5) + 1) if all(num % divisor for divisor in range(2, num))]

if N > 1:
    if N == 2 or N == 3:
        print(N)
    else:
        factors = []
        for prime in primes:
            while(N % prime == 0):
                factors.append(prime)
                N /= prime
            if N == 1:
                break
        if N != 1:
            factors.append(int(N))
        for factor in factors:
            print(factor)