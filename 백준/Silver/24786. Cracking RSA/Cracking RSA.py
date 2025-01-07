import sys
input = sys.stdin.readline

def seive(n):
    prime = [True] * (n + 1)
    p = 2
    while p*p <= n:
        if prime[p]:
            for i in range(p*p, n + 1, p):
                prime[i] = False
        p += 1
    return [i for i in range(2, n + 1) if prime[i]]

primes = seive(1000)
dic = {p * q: (p - 1) * (q - 1) for p in primes for q in primes if p != q}
for _ in range(int(input())):
    n, e = map(int, input().split())
    print(pow(e, -1, dic[n]))