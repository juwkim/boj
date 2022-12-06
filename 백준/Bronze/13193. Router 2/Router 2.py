g = lambda: [*map(int, input().split())]

from math import isqrt
N, M, P = g()
K = isqrt(N)
r, q = divmod(N, K)
print(2 * N + K, 2 * N + K - 1)
s = 1
for i in range(2*N+1, 2*N+K+1):
    if i == 2*N+K:
        for j in range(s, s + r + q):
            print(j, i)
        for j in range(N + 1, 2 * N + 1):
            print(i, j)
    else:
        print(i, i+1)
        for j in range(s, s + r):
            print(j, i)
        s += r