import sys
input = sys.stdin.readline

def sieve(N):
    primes = [False, False] + [True] * (N - 1)
    for i in range(2, int(N**.5) + 1):
        if primes[i] == False:
            continue
        for j in range(i * i, N + 1, i):
            primes[j] = False
    return [i for i in range(2, N + 1) if primes[i]]

P = int(input())
primes = sieve(223)
dp = [0] * 48
dp[0] = 1
for i in range(46):
    j = i + 1
    while primes[j] - primes[i] <= 14:
        dp[j] += dp[i]
        j += 1
print(dp[primes.index(P)])