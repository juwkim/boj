import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

for _ in range(int(input())):
    dp = bytearray(200)
    n = int(input())
    bricks = [g() for _ in range(n)]
    total = sum(t for t, _ in bricks)
    for _ in range(n):
        t, w = bricks[_]
        for i in range(total, t + w - 1, -1):
            dp[i] = max(dp[i], dp[i-t-w] + t)
    print(total - dp[total])