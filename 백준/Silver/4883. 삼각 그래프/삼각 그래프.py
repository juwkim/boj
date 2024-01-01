import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

tc = 1
while N:=int(input()):
    dp = g()
    dp[0] = 10**9
    if dp[2] > 0:
        dp[2] = 10**9
    else:
        dp[2] += dp[1]
    for _ in range(N - 1):
        new = g()
        new[0] += min(dp[0], dp[1])
        new[1] += min(min(dp), new[0])
        new[2] += min(dp[1], dp[2], new[1])
        dp = new
    print(f"{tc}. {dp[1]}")
    tc += 1