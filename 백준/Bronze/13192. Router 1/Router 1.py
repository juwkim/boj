g = lambda: [*map(int, input().split())]

from math import isqrt
N, M, P = g()
K = isqrt(N) + 2
r, q = divmod(N, K-1)
print(2 * N + K, N + N * K)
s = 1
e = N + 1
for i in range(2*N+1, 2*N+K+1):
    if i == 2 * N + K:
        for j in range(s, s + q):
            print(j, i)
        for j in range(e, e + N):
            print(i, j)
    else:
        for j in range(s, s + r):
            print(j, i)
        for j in range(e, e + N):
            print(i, j)
        s += r