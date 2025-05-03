for l in open(0):
    k, n = map(int, l.split())
    dp = [[0] * (k + 1) for _ in range(n + 1)]
    for i in range(k + 1):
        dp[1][i] = 1
    for length in range(2, n + 1):
        for digit in range(k + 1):
            dp[length][digit] = dp[length - 1][digit]
            if digit > 0: dp[length][digit] += dp[length - 1][digit - 1]
            if digit < k: dp[length][digit] += dp[length - 1][digit + 1]
    print(f"{100 * sum(dp[n]) / (k + 1) ** n:.5f}")