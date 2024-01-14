import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

def sieve(N):
    primes = [False, False] + [True] * (N - 1)
    for i in range(2, int(N**.5) + 1):
        if primes[i] == False:
            continue
        for j in range(i * i, N + 1, i):
            primes[j] = False
    return [i for i in range(N + 1) if primes[i]]

N = int(input())
primes = sieve(48611)
print(*primes[:N])