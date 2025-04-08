import sys
g = lambda: [*map(int, sys.stdin.readline().split())]

H, W = g()
B1 = [g() for _ in range(H)]
B2 = [g() for _ in range(H)]
dp = [(a - b) ** 2 for a, b in zip(B1[0], B2[0])]
for i in range(1, H):
    new = [(a - b) ** 2 for a, b in zip(B1[i], B2[i])]
    for j in range(W):
        if j == 0:
            new[j] += dp[0] if W == 1 else min(dp[0], dp[1])
        elif j == W - 1:
            new[j] += min(dp[-1], dp[-2])
        else:
            new[j] += min(dp[j - 1], dp[j], dp[j + 1])
    dp = new
print(min(dp))