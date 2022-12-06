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

def check(prime):
    dic = {}
    while not dic.get(prime):
        dic[prime] = 1
        prime = sum(int(i)**2 for i in str(prime))
        if prime == 1:
            return True
    return False

N = int(input())
primes = Sieve_of_Eratosthenes(N)
for prime in primes:
    if check(prime):
        print(prime)