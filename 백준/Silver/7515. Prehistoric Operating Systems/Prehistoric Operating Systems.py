dp = [(1, 1)]
for i in range(39):
    dp.append((sum(dp[-1]), dp[-1][0]))

for t in range(1, 1 + int(input())):
    print(f'Scenario {t}:\n{sum(dp[int(input()) - 1])}\n')