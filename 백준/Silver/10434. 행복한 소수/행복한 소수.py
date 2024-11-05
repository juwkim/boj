import sys
input = sys.stdin.readline

def sieve(n):
    p = [True] * (n + 1)
    p[0] = p[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if p[i]:
            for j in range(i * i, n + 1, i):
                p[j] = False
    return p

primes = sieve(10000)
for _ in range(int(input())):
    tc, M = map(int, input().split())
    ans = "NO"
    num = M
    if primes[num]:
        visited = set()
        while num != 1 and num not in visited:
            visited.add(num)
            num = sum(int(i) ** 2 for i in str(num))
        if num == 1:
            ans = "YES"
    print(tc, M, ans)