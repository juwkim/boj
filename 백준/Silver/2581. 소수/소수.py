M, N = int(input()), int(input())
primes = [num for num in range(M, N + 1) if all(num % divisor for divisor in range(2, num))]
if 1 in primes:
    primes.remove(1)
if not len(primes):
    print(-1)
else:
    print(sum(primes))
    print(primes[0])