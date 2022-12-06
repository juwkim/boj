dp = [1, 1] + [0] * 249
for i in range(249):
    dp[i+2] = dp[i+1] + 2 * dp[i]

while True:
    try:
        print(dp[int(input())])
    except:
        break