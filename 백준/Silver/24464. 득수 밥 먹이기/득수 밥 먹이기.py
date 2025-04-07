a, b, c, d, e = 1, 1, 1, 1, 1
mod = 1000000007
for _ in range(int(input()) - 1):
    a, b, c, d, e = (b + c + d + e) % mod, (a + d + e) % mod, (a + e) % mod, (a + b) % mod, (a + b + c) % mod
print((a + b + c + d + e) % mod)