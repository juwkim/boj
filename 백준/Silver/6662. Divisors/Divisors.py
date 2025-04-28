n = 431
is_prime = [True] * (n + 1)
is_prime[0] = is_prime[1] = False
primes = []
for i in range(2, n + 1):
    if is_prime[i]:
        primes.append(i)
        for j in range(i * i, n + 1, i):
            is_prime[j] = False

def solve(n, p):
    cnt = 0
    while n:
        n //= p
        cnt += n
    return cnt

for line in open(0):
    n, k = map(int, line.split())
    ans = 1
    for p in primes:
        if p > n:
            break
        ans *= solve(n, p) - solve(k, p) - solve(n - k, p) + 1
    print(ans)