def f(s):
    if len(s) == 1:
        return int(s)
    res, prev = 0, 0
    for i, c in enumerate(map(int, s)):
        if c > prev:
            res += sum(dp[len(s) - i][9 - j] for j in range(prev, c))
            res %= MOD
            prev = c
        elif c < prev:
            return res
    return res + 1

L, R = input(), input()
N, MOD = len(R), 10 ** 9 + 7
dp = [[0] * 10 for _ in range(N + 1)]
dp[1] = [1] * 9 + [0]
for i in range(1, N):
    Sum = 0
    for j in range(10):
        Sum += dp[i][j]
        dp[i + 1][j] = Sum
print((f(R) - f(str(int(L) - 1))) % MOD)