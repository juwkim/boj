import sys
g = lambda: map(int, sys.stdin.readline().split())

for _ in range(int(input())):
    n, W = g()
    dp = [0] * (W + 1)
    for _ in range(n):
        w, v = g()
        for i in range(W, w - 1, -1):
            dp[i] = max(dp[i], dp[i - w] + v)
    print(max(dp))