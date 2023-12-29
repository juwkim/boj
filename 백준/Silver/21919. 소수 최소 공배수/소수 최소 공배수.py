import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

def sieve(N):
    primes = [False, False] + [True] * (N - 1)
    for i in range(2, int(N ** 0.5) + 1):
        if primes[i] == False:
            continue
        for j in range(i * i, N + 1, i):
            primes[j] = False
    return primes

input()
primes = sieve(1000000)
Set = set()
for num in g():
    if primes[num]:
        Set.add(num)
if Set:
    ans = 1
    for num in Set:
        ans *= num
else:
    ans = -1
print(ans)