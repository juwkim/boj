import sys
input = sys.stdin.readline

mod = 1_000_000_009
dp = [(), (1, 0, 0), (0, 1, 0), (1, 1, 1)]
for _ in range(10**5 - 3):
    dp.append((sum(dp[-1][1:]) % mod, (dp[-2][0] + dp[-2][2]) % mod, sum(dp[-3][:2]) % mod))
for _ in range(int(input())):
    print(sum(dp[int(input())]) % mod)