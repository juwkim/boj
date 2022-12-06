dp = [0, 1, 2, 4]
for _ in range(10**6 - 3):
    dp.append(sum(dp[-3:]) % 1_000_000_009)
for _ in range(int(input())):
    print(dp[int(input())])