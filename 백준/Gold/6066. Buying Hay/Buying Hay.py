g = lambda: [*map(int, input().split())]
N, H = g()
items = [g() for _ in range(N)]
MAX_WEIGHT = H + max(p for p, c in items)
dp = [1e9] * MAX_WEIGHT
dp[0] = 0
for p, c in items:
    for w in range(p, MAX_WEIGHT):
        dp[w] = min(dp[w], dp[w - p] + c)
print(min(dp[H:]))