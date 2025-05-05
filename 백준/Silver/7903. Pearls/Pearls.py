import sys
input = sys.stdin.readline

for _ in range(int(input())):
    c = int(input())
    a, p = zip(*[map(int, input().split()) for _ in range(c)])
    px = [0]
    dp = [0]
    for i in range(c):
        px.append(px[-1] + a[i])
        dp.append(p[i] * (px[-1] + 10))
    for i in range(1, c + 1):
        for j in range(1, i + 1):
            dp[i] = min(dp[i], (px[i] - px[j] + 10) * p[i - 1] + dp[j])
    print(dp[-1])