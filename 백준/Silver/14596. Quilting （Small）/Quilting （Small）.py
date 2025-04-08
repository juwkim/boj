import sys
g = lambda: [*map(int, sys.stdin.readline().split())]

H, W = g()
B1 = [g() for _ in range(H)]
B2 = [g() for _ in range(H)]
dp = [1e9] + [(a - b) ** 2 for a, b in zip(B1[0], B2[0])] + [1e9]
for i in range(1, H):
    new = [1e9] + [(a - b) ** 2 for a, b in zip(B1[i], B2[i])] + [1e9]
    for j in range(1, W + 1):
        new[j] += min(dp[j-1:j+2])
    dp = new
print(min(dp))