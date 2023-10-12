import sys
input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

N, M, T, K = g()
n = (K + T - 1) // T
q, r = divmod(N, M)
if q >= n:
    ans = M * n * (2 * K - T * (n - 1)) // 2
else:
    ans = M * q * (2 * K - T * (q - 1)) // 2 + (K - T * q) * r
print(ans)