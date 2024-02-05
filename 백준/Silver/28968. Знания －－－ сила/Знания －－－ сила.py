n, k = map(int, input().split())
a, b = 0, n
MOD = 10 ** 9 + 7
for _ in range(k):
    a, b = (2 * a + b) % MOD, (a + b) % MOD
print((a + b) % MOD)