import sys
g = lambda: map(int, sys.stdin.readline().split())
from math import isqrt

N, M = g()
K = isqrt(N)
matchbox = [0] * N
cup = (N + K - 1) // K * [0]

for _ in range(M):
    S, A = g()
    l, r = A - 1, A - 1 + S
    ans = 0
    while l < r and l % K:
        matchbox[l] += 1
        ans += matchbox[l]
        l += 1
    if r != N:
        while l < r and r % K:
            r -= 1
            matchbox[r] += 1
            ans += matchbox[r]
    for i in range(l, r, K):
        cup[i // K] += 1
        ans += cup[i // K]
    print(ans)