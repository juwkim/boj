def seive(n):
    p = [True] * (n + 1)
    p[0] = p[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if p[i]:
            for j in range(i * i, n + 1, i):
                p[j] = False
    primes = [i for i in range(2, n + 1) if p[i]]
    return p, primes

isprime, primes = seive(15000)
l = len(primes)
for T in map(int, [*open(0)][:-1]):
    ans = 0
    for i in range(l):
        p = primes[i]
        for j in range(i, l):
            q = primes[j]
            r = T - p - q
            if r >= p + q:
                continue
            if r < q:
                break
            ans += isprime[r]
    print(ans)