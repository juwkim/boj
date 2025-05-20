MOD = 1_000_000_007
N = int(input())
ans = 0
phi = pow(24, -2, MOD)
comb, p, q = 1, 1, pow(24, N, MOD)
for i in range(0, N + 1, 2):
    ans = (ans + comb * p * q) % MOD
    p, q = p * 4 % MOD, q * phi % MOD
    comb = comb * (N - i) * (N - i - 1) * pow((i + 1) * (i + 2), -1, MOD) % MOD
print(ans)