import sys
g = lambda: [*map(int, sys.stdin.readline().split())]

m = 10**9 + 7
N, M = g()
i = sum(g()[1] for _ in range(N))
ans = pow(M - 1, i, m) * (1 + (N - i) * (M - 1))
if i: ans += i * pow(M - 1, i - 1, m)
print(ans % m)