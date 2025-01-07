from bisect import bisect

def seive(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
    return [i for i in range(2, n + 1) if is_prime[i]]

primes = seive(101000)
for N, P in map(lambda s: map(int, s.split()), [*open(0)][:-1]):
    idx = bisect(primes, N)
    nums = sorted(primes[i] + primes[j] for i in range(idx, idx + 25) for j in range(i, idx + 25))
    print(nums[P - 1])