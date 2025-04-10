import sys
g = lambda: [*map(int, sys.stdin.readline().split())]

mod = 1000000007
N, M = g()
cnt = sum(g()[1] for _ in range(N))
ans = pow(M - 1, cnt, mod) + (N - cnt) * pow(M - 1, cnt + 1, mod)
if cnt:
    ans += cnt * pow(M - 1, cnt - 1, mod)
print(ans % mod)