g = lambda: [*map(int, input().split())]

H, Y = g()
dp = [H] + [0] * (Y + 4)
for i in range(1, Y+1):
    A = int(dp[i-1] * 1.05)
    B = int(dp[i-3] * 1.20)
    C = int(dp[i-5] * 1.35)
    dp[i] = max(A, B, C)
print(dp[Y])