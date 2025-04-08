import sys
g = lambda: [*map(int, sys.stdin.readline().split())]

H, W = g()
B1 = [g() for _ in range(H)]
B2 = [g() for _ in range(H)]
dp = [0] * (W + 2)
for i in range(H):
    dp = [1e9] + [(B1[i][j] - B2[i][j])**2 + min(dp[j:j+3]) for j in range(W)] + [1e9]
print(min(dp))