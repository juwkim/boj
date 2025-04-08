import sys
g = lambda: [*map(int, sys.stdin.readline().split())]

H, W = g()
B1 = [g() for _ in range(H)]
B2 = [g() for _ in range(H)]
dp = [1e9] + [(a - b) ** 2 for a, b in zip(B1[0], B2[0])] + [1e9]
for i in range(1, H):
    dp = [1e9] + [(B1[i][j] - B2[i][j])**2 + min(dp[j:j+3]) for j in range(W)] + [1e9]
print(min(dp))