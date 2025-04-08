N, M = map(int, input().split())
mod = 1_000_000_007
dp = [1] * 26
for _ in range(M - 1):
    new = [0] * 26
    for i in range(26):
        for j in range(26):
            if abs(i - j) >= N:
                new[j] = (new[j] + dp[i]) % mod
    dp = new
print(sum(dp) % mod)