a = [1] * 10
dp = [0, 10]
for _ in range(999):
    a = [a[7], a[2] + a[4], a[1] + a[3] + a[5], a[2] + a[6], a[1] + a[5] + a[7], a[2] + a[4] + a[6] + a[8], a[3] + a[5] + a[9], a[0] + a[4] + a[8], a[5] + a[7] + a[9], a[6] + a[8]]
    dp.append(sum(a) % 1234567)
for _ in range(int(input())):
    print(dp[int(input())])