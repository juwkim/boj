def seive(n):
    p = [1] * (n + 1)
    p[0] = p[1] = 0
    for i in range(2, int(n ** 0.5) + 1):
        if p[i]:
            for j in range(i * i, n + 1, i):
                p[j] = 0
    return p, [i for i in range(2, n + 1) if p[i]]

N, *a = map(int, open(0).read().split())
px = [0] * (N + 1)
for i in range(N):
    px[i + 1] = px[i] + a[i]
is_prime, primes = seive(1000000)
ans = 0
for l in range(2, N + 1):
    if not is_prime[l]:
        continue
    ans += sum(is_prime[px[i + l] - px[i]] for i in range(N - l + 1))
print(ans)