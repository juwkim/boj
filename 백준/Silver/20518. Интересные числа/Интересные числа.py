def f(s):
    res, prev = 0, 0
    for i, c in enumerate(map(int, s)):
        if c > prev:
            res += sum(dp[len(s) - i][10 - j] for j in range(prev, c))
            res %= MOD
            prev = c
        else:
            break
    return res

L, R = input(), input()
N, MOD = len(R), 10 ** 9 + 7
dp = [[0] * 11 for _ in range(N + 2)]
dp[1] = [0] + [1] * 9 + [0]
for i in range(1, N + 1):
    Sum = 0
    for j in range(1, 11):
        Sum += dp[i][j]
        dp[i + 1][j] = Sum
print((f(R) - f(str(int(L) - 1))) % MOD)