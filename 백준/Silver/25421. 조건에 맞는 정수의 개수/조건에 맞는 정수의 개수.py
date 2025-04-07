dp = [0] * 2 + [1] * 9 + [0] * 2
for _ in range(int(input()) - 1):
    new = [0] * 13
    for i in range(2, 11):
        new[i] = sum(dp[i-2:i+3]) % 987654321
    dp = new
print(sum(dp) % 987654321)