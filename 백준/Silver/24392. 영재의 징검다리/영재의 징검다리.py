import sys
g = lambda: [*map(int, sys.stdin.readline().split())]
mod = 10**9 + 7
N, M = g()
dp = [0] + g() + [0]
for _ in range(N - 1):
    new = [0] * (M + 2)
    for i, c in enumerate(g(), 1):
        if c:
            new[i] = sum(dp[i-1:i+2]) % mod
    dp = new
print(sum(dp) % mod)