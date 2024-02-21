import sys
input = sys.stdin.readline

def sieve(N):
    primes = [False, False] + [True] * (N - 1)
    for i in range(2, int(N**.5) + 1):
        if primes[i] == False:
            continue
        for j in range(i * i, N + 1, i):
            primes[j] = False
    return primes

ans = [False, False]
prime = sieve(10000)
for num in range(2, 10001):
    cnt = 0
    for i in range(1, int(num**.5) + 1):
        q, r = divmod(num, i)
        if r == 0:
            cnt += 1
            if i != q:
                cnt += 1
    if prime[cnt]:
        ans.append(True)
    else:
        ans.append(False)
for _ in range(int(input())):
    L, H = map(int, input().split())
    buf = [i for i in range(L, H + 1) if ans[i]]
    if buf:
        print(*buf)
    else:
        print(-1)