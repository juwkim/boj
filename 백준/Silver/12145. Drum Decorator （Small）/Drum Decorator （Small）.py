import sys
input = sys.stdin.readline
from math import lcm

MOD = 10**9 + 7
for tc in range(1, 1 + int(input())):
    R, C = map(int, input().split())
    dp = [[[0] * 13, [0] * 13] for i in range(R + 1)]
    dp[0][0][1], dp[0][1][1] = 1, 1
    for i in range(R):
        for degree, p in enumerate(dp[i][0]):
            if p == 0:
                continue
            if i + 2 <= R:
                dp[i + 2][1][degree] = (dp[i + 2][1][degree] + p) % MOD
        for degree, p in enumerate(dp[i][1]):
            if p == 0:
                continue
            if i + 1 <= R:
                dp[i + 1][0][degree] = (dp[i + 1][0][degree] + p) % MOD
            if i + 2 <= R:
                if C % 3 == 0:
                    dp[i + 2][0][lcm(degree, 3)] = (dp[i + 2][0][lcm(degree, 3)] + 3 * p) % MOD
                if C % 6 == 0:
                    dp[i + 2][0][lcm(degree, 6)] = (dp[i + 2][0][lcm(degree, 6)] + 6 * p) % MOD
            if i + 3 <= R and C % 4 == 0:
                dp[i + 3][0][lcm(degree, 4)] = (dp[i + 3][0][lcm(degree, 4)] + 4 * p) % MOD
    ans = 0
    for t in range(2):
        for degree, p in enumerate(dp[R][t]):
            if p == 0:
                continue
            ans = (ans + p // degree) % MOD
    print(f'Case #{tc}: {ans}')