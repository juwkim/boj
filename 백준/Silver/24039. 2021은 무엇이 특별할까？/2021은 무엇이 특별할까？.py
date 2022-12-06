def shieve(n):
    a = [False,False] + [True] * (n-1)
    primes = []
    for i in range(2, n + 1):
        if a[i]:
            primes.append(i)
            for j in range(2 * i, n + 1, i):
                a[j] = False
    return primes

primes = shieve(103)
N = int(input())
for i in range(102):
    ans = primes[i] * primes[i+1]
    if ans > N:
        break
print(ans)