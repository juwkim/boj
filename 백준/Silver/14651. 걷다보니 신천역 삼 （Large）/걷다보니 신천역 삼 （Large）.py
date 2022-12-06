mod = 1_000_000_009
n = int(input())
if n == 1:
    print(0)
else:
    a = 2 * pow(3, n - 2, mod) % mod
    print(a)