MOD = int(1e9 + 7)

def solve(s):
    n = len(s)
    dp = [[[[0 for _ in range(4)] for _ in range(n//2 + 2)] for _ in range(n//2 + 2)] for _ in range(n + 1)]
    dp[0][0][0][0] = 1

    for i in range(n):
        for j in range(n // 2 + 1):
            for k in range(n // 2 + 1):
                if sum(dp[i][j][k]) == 0:
                    continue
                # situation 0
                dp[i + 1][j][k][0] = (dp[i + 1][j][k][0] + dp[i][j][k][0]) % MOD
                if s[i] == 'a':
                    dp[i + 1][j + 1][k][0] = (dp[i + 1][j + 1][k][0] + dp[i][j][k][0]) % MOD
                elif s[i] == 'b' and j > 0:
                    dp[i + 1][j][k + 1][1] = (dp[i + 1][j][k + 1][1] + dp[i][j][k][0]) % MOD

                # situation 1
                dp[i + 1][j][k][1] = (dp[i + 1][j][k][1] + dp[i][j][k][1]) % MOD
                if s[i] == 'b':
                    dp[i + 1][j][k + 1][1] = (dp[i + 1][j][k + 1][1] + dp[i][j][k][1]) % MOD
                elif s[i] == 'c':
                    if j == 1:
                        dp[i + 1][0][k][3] = (dp[i + 1][0][k][3] + dp[i][j][k][1]) % MOD
                    else:
                        dp[i + 1][j - 1][k][2] = (dp[i + 1][j - 1][k][2] + dp[i][j][k][1]) % MOD

                # situation 2
                dp[i + 1][j][k][2] = (dp[i + 1][j][k][2] + dp[i][j][k][2]) % MOD
                if s[i] == 'c':
                    if j == 1:
                        dp[i + 1][0][k][3] = (dp[i + 1][0][k][3] + dp[i][j][k][2]) % MOD
                    else:
                        dp[i + 1][j - 1][k][2] = (dp[i + 1][j - 1][k][2] + dp[i][j][k][2]) % MOD

                # situation 3
                dp[i + 1][j][k][3] = (dp[i + 1][j][k][3] + dp[i][j][k][3]) % MOD
                if s[i] == 'd':
                    if k == 1:
                        dp[i + 1][0][0][0] = (dp[i + 1][0][0][0] + dp[i][j][k][3]) % MOD
                    else:
                        dp[i + 1][0][k - 1][3] = (dp[i + 1][0][k - 1][3] + dp[i][j][k][3]) % MOD

    return (dp[n][0][0][0] - 1) % MOD

for cas in range(1, int(input()) + 1):
    print(f"Case #{cas}: {solve(input())}")