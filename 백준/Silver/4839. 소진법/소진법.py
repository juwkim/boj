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

primes = sieve_of_eratosthenes(30)
while N := int(input()):
    ans, i, cur = [], 0, N
    while cur:
        cur, r = divmod(cur, primes[i])
        ans.append(r)
        i += 1
    buf = []
    for i in range(len(ans)):
        if ans[i]:
            buf.append('*'.join(map(str, [ans[i]] + primes[:i])))
    print(N, '=', ' + '.join(buf))