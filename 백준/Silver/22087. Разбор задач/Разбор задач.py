for _ in range(int(input())):
    n, m, t, c = map(int, input().split())
    dp = [m] * n
    for s in zip(*[input() for _ in range(n)]):
        dp = [min(dp[j] - (i == j) for j in range(n)) if ch == '1' else m for i, ch in enumerate(s)]
    print(m * t + c * min(dp))