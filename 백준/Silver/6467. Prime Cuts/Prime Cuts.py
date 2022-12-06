g = lambda: [*map(int, input().split())]

from math import isqrt
def prime_list(n):
    sieve = [True] * (n + 1)

    for i in range(2, isqrt(n) + 1):
        if sieve[i] == True:           # i가 소수인 경우
            for j in range(i*i, n+1, i): # i이후 i의 배수들을 False 판정
                sieve[j] = False

    # 소수 목록 산출
    return [i for i in range(2, n+1) if sieve[i]]

from bisect import bisect_right
primes = [1] + prime_list(1000)
while True:
    try:
        N, C = g()
        idx = bisect_right(primes, N)
        p = idx // 2
        print(f'{N} {C}:', *primes[max(0, p-C+idx%2):min(idx,p+C)])
        print()
    except:
        break